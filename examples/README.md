# Example PDFs and usage

This directory contains example PDF files for testing the PdftoWordAgent.

## Adding Examples

To test the tool with your own PDFs:

```bash
# Copy your PDF here
cp /path/to/your/document.pdf examples/

# Convert it
python main.py convert examples/document.pdf -o examples/document.docx
```

## Sample Conversion Commands

```bash
# Convert with default settings
python main.py convert examples/sample.pdf

# Convert with custom output
python main.py convert examples/sample.pdf -o examples/output.docx

# Preview formatting
python main.py preview examples/sample.pdf --verbose

# View settings
python main.py config
```

See [../README.md](../README.md) for complete usage documentation.
