"""
PDF text extraction with formatting preservation (bold, italic, underline)
"""

import logging
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import pdfplumber
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class StyledText:
    """Represents a text segment with its styling"""
    text: str
    bold: bool = False
    italic: bool = False
    underline: bool = False
    font_size: Optional[float] = None
    font_name: Optional[str] = None
    
    def has_style(self) -> bool:
        """Check if text has any styling"""
        return self.bold or self.italic or self.underline


@dataclass
class PDFPage:
    """Represents a single page from PDF"""
    page_number: int
    text_segments: List[StyledText]
    width: float
    height: float
    
    def get_plain_text(self) -> str:
        """Get plain text without styling"""
        return "".join(segment.text for segment in self.text_segments)


class PDFExtractor:
    """Extract text with styling from PDF files"""
    
    def __init__(self, font_size_threshold: float = 0.2):
        """
        Initialize PDF extractor
        
        Args:
            font_size_threshold: Threshold for detecting bold/larger text (percentage above average)
        """
        self.font_size_threshold = font_size_threshold
    
    def extract(self, pdf_path: str) -> List[PDFPage]:
        """
        Extract text with styling from PDF
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            List of PDFPage objects containing styled text
            
        Raises:
            FileNotFoundError: If PDF file doesn't exist
            Exception: If PDF is encrypted or corrupted
        """
        pdf_path = Path(pdf_path)
        
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        logger.info(f"Extracting text from: {pdf_path}")
        pages = []
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                logger.info(f"Processing {len(pdf.pages)} pages")
                
                for page_num, page in enumerate(pdf.pages, 1):
                    try:
                        pdf_page = self._extract_page(page, page_num)
                        pages.append(pdf_page)
                        logger.debug(f"Extracted page {page_num}")
                    except Exception as e:
                        logger.warning(f"Error extracting page {page_num}: {e}")
                        # Continue with other pages
                        continue
            
            logger.info(f"Successfully extracted {len(pages)} pages")
            return pages
            
        except Exception as e:
            logger.error(f"Failed to extract PDF: {e}")
            raise
    
    def _extract_page(self, page, page_number: int) -> PDFPage:
        """
        Extract text and styling from a single page
        
        Args:
            page: pdfplumber page object
            page_number: Current page number
            
        Returns:
            PDFPage object with styled text segments
        """
        text_segments = []
        
        # Get characters from the page
        chars = page.chars
        
        if not chars:
            # Fallback to plain text extraction if no character-level data
            plain_text = page.extract_text() or ""
            if plain_text:
                text_segments.append(StyledText(text=plain_text))
            return PDFPage(
                page_number=page_number,
                text_segments=text_segments,
                width=page.width,
                height=page.height
            )
        
        # Calculate average font size for comparison
        font_sizes = [char.get("size", 0) for char in chars if char.get("size")]
        avg_font_size = sum(font_sizes) / len(font_sizes) if font_sizes else 0
        
        # Group characters by text run
        current_segment = self._create_styled_text_from_chars(
            chars[:1] if chars else [],
            avg_font_size
        )
        
        for char in chars[1:]:
            # Check if styling changed
            char_styled = self._create_styled_text_from_chars([char], avg_font_size)
            
            if self._should_break_segment(current_segment, char_styled, char):
                # New segment
                text_segments.append(current_segment)
                current_segment = char_styled
            else:
                # Append to current segment
                current_segment.text += char.get("text", "")
        
        # Add final segment
        if current_segment.text:
            text_segments.append(current_segment)
        
        return PDFPage(
            page_number=page_number,
            text_segments=text_segments,
            width=page.width,
            height=page.height
        )
    
    def _create_styled_text_from_chars(
        self, 
        chars: List[Dict], 
        avg_font_size: float
    ) -> StyledText:
        """
        Create a StyledText object from character data
        
        Args:
            chars: List of character dictionaries from pdfplumber
            avg_font_size: Average font size of the page
            
        Returns:
            StyledText object with detected styling
        """
        if not chars:
            return StyledText(text="")
        
        char = chars[0]
        text = char.get("text", "")
        font_name = char.get("fontname", "").lower()
        font_size = char.get("size", avg_font_size)
        
        # Detect bold
        bold = "bold" in font_name or font_size > avg_font_size * (1 + self.font_size_threshold)
        
        # Detect italic
        italic = "italic" in font_name or "oblique" in font_name
        
        # Detect underline (requires more advanced parsing, often indicated in font features)
        underline = "underline" in font_name
        
        return StyledText(
            text=text,
            bold=bold,
            italic=italic,
            underline=underline,
            font_size=font_size,
            font_name=font_name
        )
    
    def _should_break_segment(
        self, 
        current: StyledText, 
        next_char: StyledText, 
        char_data: Dict
    ) -> bool:
        """
        Determine if styling changed and segment should break
        
        Args:
            current: Current styled text segment
            next_char: Next character's styling
            char_data: Raw character data from pdfplumber
            
        Returns:
            True if segment should break, False otherwise
        """
        # Break on newlines or significant whitespace changes
        if char_data.get("text") == "\n":
            return True
        
        # Break if styling changed
        if (current.bold != next_char.bold or
            current.italic != next_char.italic or
            current.underline != next_char.underline):
            return True
        
        # Break if font changed significantly
        if current.font_name != next_char.font_name:
            return True
        
        return False
