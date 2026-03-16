"""
Configuration settings for PdftoWordAgent
"""

from enum import Enum
from pathlib import Path

# Default project paths
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"

# Output directory configuration
OUTPUT_DIR.mkdir(exist_ok=True)


class FontStyle(Enum):
    """Font styling options"""
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    BOLD_ITALIC = "bold_italic"
    UNDERLINE = "underline"


class PDFExtractionConfig:
    """Configuration for PDF extraction"""
    # Minimum font size to consider for bold/italic detection
    MIN_FONT_SIZE_THRESHOLD = 0.2  # 20% larger than average
    
    # Text encoding
    ENCODING = "utf-8"
    
    # Page margin preservation (in inches)
    DEFAULT_MARGIN_TOP = 1.0
    DEFAULT_MARGIN_BOTTOM = 1.0
    DEFAULT_MARGIN_LEFT = 1.0
    DEFAULT_MARGIN_RIGHT = 1.0


class WordDocumentConfig:
    """Configuration for Word document generation"""
    # Default font settings
    DEFAULT_FONT_NAME = "Calibri"
    DEFAULT_FONT_SIZE = 11  # in points
    DEFAULT_FONT_COLOR = "000000"  # Black
    
    # Margins (in inches)
    MARGIN_TOP = 1.0
    MARGIN_BOTTOM = 1.0
    MARGIN_LEFT = 1.0
    MARGIN_RIGHT = 1.0
    
    # Line spacing
    LINE_SPACING = 1.15
    
    # Paragraph spacing (in points)
    SPACE_BEFORE = 0
    SPACE_AFTER = 6
