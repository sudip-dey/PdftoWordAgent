# PdftoWordAgent

A powerful command-line tool to convert PDF documents to Word format with intelligent preservation of text formatting (bold, italic, underline) and page layout.

## Features

✨ **Text Formatting Preservation**
- Detects and preserves **bold** text
- Detects and detects **italic** text
- Detects and preserves **underlined** text
- Automatic font size analysis for style detection

📄 **Layout Management**
- Preserves page margins
- Maintains text flow and paragraph structure
- Converts multi-page PDFs with automatic page breaks

🎯 **Smart PDF Processing**
- Handles text-only PDFs efficiently
- Character-level font analysis
- Intelligent paragraph and segment detection
- Fallback processing for complex PDFs

⚡ **User-Friendly CLI**
- Simple command-line interface
- Multiple conversion options
- Preview functionality to inspect formatting
- Verbose logging for debugging
- Progress indicators and informative output

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### From Source

```bash
git clone https://github.com/sudip-dey/PdftoWordAgent.git
cd PdftoWordAgent
pip install -r requirements.txt
```

### As a Package

```bash
pip install -e .
```

This installs the `pdftoword` command globally.

## Usage

### Basic Conversion

Convert a PDF to a Word document:

```bash
python main.py convert document.pdf
```

The output will be saved to `output/document/document.docx` by default.

### Custom Output Path

Specify where to save the converted document:

```bash
python main.py convert document.pdf -o my_document.docx
```

### Preview Mode

Preview formatting detection before conversion:

```bash
python main.py preview document.pdf
```

View detailed formatting information:

```bash
python main.py preview document.pdf --verbose
```

### Verbose Logging

Enable detailed logging for debugging:

```bash
python main.py convert document.pdf --verbose
```

### Show Configuration

Display current settings:

```bash
python main.py config
```

## Command Reference

### convert

Convert PDF to Word document.

**Usage:**
```bash
python main.py convert PDF_FILE [OPTIONS]
```

**Options:**
- `-o, --output TEXT` - Output Word file path
- `--preserve-layout` - Preserve page layout and margins (default: True)
- `-v, --verbose` - Enable verbose logging

**Examples:**
```bash
python main.py convert document.pdf
python main.py convert document.pdf -o output.docx
python main.py convert document.pdf --preserve-layout --verbose
```

### preview

Preview PDF content and detected formatting.

**Usage:**
```bash
python main.py preview PDF_FILE [OPTIONS]
```

**Options:**
- `-v, --verbose` - Show detailed page information

**Examples:**
```bash
python main.py preview document.pdf
python main.py preview document.pdf --verbose
```

### config

Show current configuration settings.

**Usage:**
```bash
python main.py config
```

## Configuration

The tool uses sensible defaults but can be customized by editing `src/config.py`:

### PDF Extraction Settings

```python
MIN_FONT_SIZE_THRESHOLD = 0.2  # 20% larger = bold/larger text
ENCODING = "utf-8"
DEFAULT_MARGIN_* = 1.0  # in inches
```

### Word Document Settings

```python
DEFAULT_FONT_NAME = "Calibri"
DEFAULT_FONT_SIZE = 11  # in points
MARGIN_* = 1.0  # in inches
LINE_SPACING = 1.15
SPACE_AFTER = 6  # points
```

## Project Structure

```
PdftoWordAgent/
├── src/
│   ├── __init__.py           # Package initialization
│   ├── cli.py                # Command-line interface
│   ├── config.py             # Configuration settings
│   ├── pdf_extractor.py      # PDF text extraction with styling
│   └── word_generator.py     # Word document generation
├── tests/                    # Unit tests
├── examples/                 # Example PDFs and outputs
├── main.py                   # Entry point
├── setup.py                  # Package setup
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore file
```

## How It Works

### 1. PDF Extraction (`pdf_extractor.py`)

- Uses **pdfplumber** for accurate PDF parsing
- Analyzes character-level font metrics
- Detects styling based on:
  - Font name (contains "bold", "italic", "underline")
  - Font size (compared to page average)
  - Font features and decorations
- Groups characters into logical text segments
- Preserves page dimensions and layout

### 2. Word Generation (`word_generator.py`)

- Uses **python-docx** for Word document creation
- Applies detected styling to text runs
- Configures page margins for layout preservation
- Maintains paragraph spacing and line height
- Sets optimal font properties for readability

### 3. CLI Interface (`cli.py`)

- Built with **Click** framework
- Provides intuitive command structure
- Offers multiple conversion modes
- Includes preview and debugging tools
- Logs all operations for transparency

## Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| PDF Processing | pdfplumber | 0.14.1 |
| Word Generation | python-docx | 0.8.11 |
| CLI Framework | Click | 8.1.7 |
| Additional | PyPDF2 | 4.0.1 |
| Language | Python | 3.8+ |

## Supported Formats

### Input
- ✅ Text-only PDFs
- ✅ PDFs with styling information
- ✅ Multi-page documents
- ✅ PDFs with margins and layout

### Output
- ✅ Microsoft Word (.docx) format
- ✅ Preserves text formatting
- ✅ Maintains page layout
- ✅ Readable in MS Word, Google Docs, LibreOffice

## Limitations

- **Text-only PDFs**: Currently optimized for PDFs containing primarily text
- **Images and graphics**: Not extracted (future enhancement)
- **Tables**: Basic table structures may not preserve exact formatting
- **Complex layouts**: Very complex multi-column layouts may require manual adjustment
- **Scanned PDFs**: OCR capabilities not included (future enhancement)

## Troubleshooting

### "PDF file not found" Error

Ensure the PDF path is correct and accessible:

```bash
# Check if file exists
ls -la document.pdf

# Use absolute path
python main.py convert /absolute/path/to/document.pdf
```

### Missing Formatting

Enable verbose mode to see what formatting is being detected:

```bash
python main.py preview document.pdf --verbose
```

Adjust `MIN_FONT_SIZE_THRESHOLD` in `src/config.py` if bold/italic detection is incorrect.

### Encoding Issues

The tool defaults to UTF-8. If you encounter encoding errors with special characters, check that your terminal supports UTF-8.

## Future Enhancements

🚀 **Planned Features**
- [ ] Table preservation and conversion
- [ ] Image extraction and embedding
- [ ] OCR support for scanned PDFs
- [ ] Multi-layout PDF support
- [ ] Header/footer preservation
- [ ] Hyperlink preservation
- [ ] Batch processing mode
- [ ] Web API interface
- [ ] GUI application

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Sudip Dey**
- GitHub: [@sudip-dey](https://github.com/sudip-dey)

## Support

For issues, questions, or suggestions:
- 📝 Open an issue on [GitHub Issues](https://github.com/sudip-dey/PdftoWordAgent/issues)
- 💬 Start a discussion on [GitHub Discussions](https://github.com/sudip-dey/PdftoWordAgent/discussions)

## Acknowledgments

- [pdfplumber](https://github.com/jsvine/pdfplumber) - PDF parsing
- [python-docx](https://python-docx.readthedocs.io/) - Word document generation
- [Click](https://click.palletsprojects.com/) - CLI framework