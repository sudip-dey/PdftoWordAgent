"""
Command-line interface for PdftoWordAgent
"""

import logging
import sys
from pathlib import Path
from typing import Optional
import click

from src.pdf_extractor import PDFExtractor
from src.word_generator import WordGenerator
from src.config import PDFExtractionConfig, WordDocumentConfig, OUTPUT_DIR

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """PdftoWordAgent - Convert PDF documents to Word format with formatting preservation"""
    pass


@cli.command()
@click.argument('pdf_file', type=click.Path(exists=True))
@click.option(
    '-o', '--output',
    type=click.Path(),
    default=None,
    help='Output Word file path (default: same name as PDF with .docx extension)'
)
@click.option(
    '--preserve-layout',
    is_flag=True,
    default=True,
    help='Preserve page layout and margins'
)
@click.option(
    '-v', '--verbose',
    is_flag=True,
    help='Enable verbose logging'
)
def convert(
    pdf_file: str,
    output: Optional[str],
    preserve_layout: bool,
    verbose: bool
):
    """
    Convert PDF to Word document
    
    Examples:
        pdftoword convert document.pdf
        pdftoword convert document.pdf -o output.docx
        pdftoword convert document.pdf --verbose
    """
    
    # Set logging level
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        pdf_path = Path(pdf_file)
        
        # Determine output path
        if output:
            output_path = Path(output)
        else:
            output_path = OUTPUT_DIR / pdf_path.stem / f"{pdf_path.stem}.docx"
        
        click.echo(f"📄 Converting: {pdf_file}")
        click.echo(f"💾 Output: {output_path}")
        
        # Extract PDF
        extractor = PDFExtractor(font_size_threshold=0.2)
        pages = extractor.extract(str(pdf_path))
        
        click.echo(f"✓ Extracted {len(pages)} pages with formatting")
        
        # Generate Word document
        generator = WordGenerator(config=WordDocumentConfig())
        word_file = generator.generate(pages, str(output_path))
        
        click.echo(f"✓ Document created: {word_file}")
        click.echo("✓ Conversion completed successfully!")
        
    except FileNotFoundError as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        if verbose:
            logger.exception("Detailed error:")
        sys.exit(1)


@cli.command()
@click.argument('pdf_file', type=click.Path(exists=True))
@click.option(
    '-v', '--verbose',
    is_flag=True,
    help='Show detailed page information'
)
def preview(pdf_file: str, verbose: bool):
    """
    Preview PDF content and detected formatting
    
    Example:
        pdftoword preview document.pdf
    """
    
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        pdf_path = Path(pdf_file)
        
        click.echo(f"📄 Previewing: {pdf_file}\n")
        
        extractor = PDFExtractor()
        pages = extractor.extract(str(pdf_path))
        
        for page in pages:
            click.echo(f"--- Page {page.page_number} ---")
            click.echo(f"Dimensions: {page.width:.1f} x {page.height:.1f}")
            click.echo(f"Text segments: {len(page.text_segments)}")
            
            if verbose:
                for i, segment in enumerate(page.text_segments):
                    styling = []
                    if segment.bold:
                        styling.append("BOLD")
                    if segment.italic:
                        styling.append("ITALIC")
                    if segment.underline:
                        styling.append("UNDERLINE")
                    
                    style_str = f" [{', '.join(styling)}]" if styling else ""
                    preview_text = segment.text[:50] + "..." if len(segment.text) > 50 else segment.text
                    click.echo(f"  [{i}] {preview_text}{style_str}")
            else:
                plain_text = page.get_plain_text()[:100]
                click.echo(f"  Preview: {plain_text}...")
            
            click.echo()
        
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)


@cli.command()
def config():
    """Show current configuration"""
    
    click.echo("PdftoWordAgent Configuration\n")
    
    click.echo("PDF Extraction Settings:")
    click.echo(f"  Font size threshold: {PDFExtractionConfig.MIN_FONT_SIZE_THRESHOLD * 100}%")
    click.echo(f"  Default margins: {PDFExtractionConfig.DEFAULT_MARGIN_TOP}\"")
    
    click.echo("\nWord Document Settings:")
    click.echo(f"  Default font: {WordDocumentConfig.DEFAULT_FONT_NAME}")
    click.echo(f"  Default font size: {WordDocumentConfig.DEFAULT_FONT_SIZE}pt")
    click.echo(f"  Line spacing: {WordDocumentConfig.LINE_SPACING}")
    click.echo(f"  Margins: {WordDocumentConfig.MARGIN_TOP}\"")
    
    click.echo(f"\nOutput directory: {OUTPUT_DIR}")


if __name__ == '__main__':
    cli()
