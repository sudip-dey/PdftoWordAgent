#!/usr/bin/env python3
"""
Setup script for PdftoWordAgent
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="pdftowordagent",
    version="0.1.0",
    description="Convert PDF documents to Word format with formatting preservation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sudip Dey",
    url="https://github.com/sudip-dey/PdftoWordAgent",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pdfplumber==0.14.1",
        "python-docx==0.8.11",
        "click==8.1.7",
        "PyPDF2==4.0.1",
    ],
    entry_points={
        "console_scripts": [
            "pdftoword=src.cli:cli",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="pdf word conversion cli tool formatting",
)
