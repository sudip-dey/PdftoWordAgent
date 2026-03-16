"""Generate a sample PDF with formatted text for testing"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

# Create PDF
pdf_path = "examples/sample_formatted.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
story = []

# Get styles
styles = getSampleStyleSheet()

# Add formatted text
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor('#1f4788'),
    spaceAfter=30,
)

normal_style = styles['Normal']
normal_style.fontSize = 11
normal_style.spaceAfter = 12

# Title
story.append(Paragraph("Sample PDF Document", title_style))
story.append(Spacer(1, 0.2*inch))

# Normal text with different formatting
story.append(Paragraph(
    "This is a <b>sample PDF</b> document with <i>formatted text</i>. "
    "It contains <b><i>bold and italic</i></b> text to test the conversion process.",
    normal_style
))
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph(
    "The next paragraph has <u>underlined text</u> to verify that underline detection works properly.",
    normal_style
))
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph(
    "<b>Bold text</b> should be detected by the PDF extractor. "
    "<i>Italic text</i> should also be properly identified. "
    "The tool preserves these styling elements when converting to Word format.",
    normal_style
))

# Build PDF
doc.build(story)
print(f"✓ Created sample PDF: {pdf_path}")
