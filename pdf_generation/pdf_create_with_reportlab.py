
# From: https://vonkunesnewton.medium.com/generating-pdfs-with-reportlab-ced3b04aedef
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# In Memory:
# pdf_buffer = BytesIO()
# my_doc = SimpleDocTemplate(pdf_buffer)

# For File:
my_doc = SimpleDocTemplate('reportlab_template.pdf')


sample_style_sheet = getSampleStyleSheet()
flowables = []
# my_doc.build(flowables)


paragraph_1 = Paragraph("A title", sample_style_sheet['Heading1'])
paragraph_2 = Paragraph(
    "Some normal body text",
    sample_style_sheet['BodyText']
)
flowables.append(paragraph_1)
flowables.append(paragraph_2)

my_doc.build(flowables)
