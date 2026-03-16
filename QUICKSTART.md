"""Quick setup and testing guide"""

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **View available commands:**
   ```bash
   python main.py --help
   ```

3. **Show configuration:**
   ```bash
   python main.py config
   ```

## Create Test PDF

Run the included script to create a sample PDF:

```bash
python create_sample_pdf.py
```

This creates `examples/sample_formatted.pdf` with formatted text.

## Test Conversion

```bash
# Preview the PDF
python main.py preview examples/sample_formatted.pdf

# Preview with detailed formatting info
python main.py preview examples/sample_formatted.pdf --verbose

# Convert to Word
python main.py convert examples/sample_formatted.pdf

# Convert with custom output path
python main.py convert examples/sample_formatted.pdf -o examples/output.docx
```

## Project Layout

```
src/
  ├── __init__.py          Package initialization
  ├── cli.py               Command-line interface
  ├── config.py            Configuration and settings
  ├── pdf_extractor.py     PDF text and formatting extraction
  └── word_generator.py    Word document creation and styling

main.py                     Entry point for the CLI
requirements.txt            Python dependencies
setup.py                    Package setup and installation
README.md                   User documentation
DEVELOPER.md               Development guidelines
```

## Key Features Implemented

✓ CLI interface with 3 commands (convert, preview, config)
✓ PDF text extraction with styling detection
✓ Bold, italic, underline preservation
✓ Page layout and margins preservation
✓ Word document generation
✓ Error handling and logging
✓ Comprehensive documentation
✓ Development setup guide

## Next Steps (Future Enhancements)

- [ ] Unit tests for extraction and generation
- [ ] Integration tests with various PDF types
- [ ] Table extraction and preservation
- [ ] Image extraction capability
- [ ] OCR support for scanned PDFs
- [ ] Batch processing mode
- [ ] Web API interface
- [ ] GUI application
