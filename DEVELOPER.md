# Development Guide

## Setting Up Development Environment

### 1. Clone the Repository

```bash
git clone https://github.com/sudip-dey/PdftoWordAgent.git
cd PdftoWordAgent
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### Optional: Install Development Tools

```bash
pip install pytest pytest-cov black flake8 mypy
```

## Project Architecture

### Core Modules

**src/pdf_extractor.py**
- `PDFExtractor` class for extracting text from PDFs
- `StyledText` dataclass for text with formatting
- `PDFPage` dataclass for organized page content
- Character-level analysis and styling detection

**src/word_generator.py**
- `WordGenerator` class for creating Word documents
- Styling application (bold, italic, underline)
- Margin and layout preservation
- Paragraph formatting

**src/config.py**
- Configuration constants
- Extraction and document generation settings
- Font and styling definitions
- Path management

**src/cli.py**
- Command-line interface using Click
- `convert` command for PDF to Word conversion
- `preview` command for formatting inspection
- `config` command for settings display

## Code Style

The project follows PEP 8 conventions:

```bash
# Format code with black
black src/ tests/

# Check style with flake8
flake8 src/ tests/ --max-line-length=100

# Type checking with mypy
mypy src/
```

## Testing

Run unit tests:

```bash
python -m pytest tests/ -v
```

With coverage:

```bash
pytest --cov=src tests/
```

## Common Development Tasks

### Adding a New Feature

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Write tests for the feature
3. Implement the feature
4. Ensure all tests pass
5. Commit: `git commit -m "Add feature: description"`
6. Push and create a pull request

### Debugging

Enable verbose logging:

```bash
python main.py convert document.pdf --verbose
```

Use preview to inspect PDF content:

```bash
python main.py preview document.pdf --verbose
```

### Performance Profiling

```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Your code here

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative').print_stats(20)
```

## Release Process

1. Update version in `src/__init__.py` and `setup.py`
2. Update CHANGELOG.md (if exists)
3. Create git tag: `git tag v0.1.0`
4. Push tag: `git push origin v0.1.0`
5. Build distribution:
   ```bash
   python -m pip install --upgrade build
   python -m build
   ```
6. Upload to PyPI (optional):
   ```bash
   python -m pip install --upgrade twine
   python -m twine upload dist/*
   ```

## Documentation

- Update README.md for user-facing changes
- Add docstrings to all public functions
- Include type hints in function signatures
- Add inline comments for complex logic

## Troubleshooting

### Import Errors

Ensure the package is in development mode:

```bash
pip install -e .
```

### PDF Extraction Issues

1. Check if pdfplumber is properly installed
2. Enable verbose logging to see character data
3. Verify PDF is not encrypted

### Word Generation Issues

1. Ensure python-docx is installed
2. Check disk space for output directory
3. Verify output path is writable

## Contributing Guidelines

1. Follow PEP 8 style guide
2. Add tests for new features
3. Update documentation
4. Keep commits atomic and well-described
5. No hardcoded paths or credentials

## Resources

- [pdfplumber Documentation](https://github.com/jsvine/pdfplumber)
- [python-docx Documentation](https://python-docx.readthedocs.io/)
- [Click Documentation](https://click.palletsprojects.com/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
