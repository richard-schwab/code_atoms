import pdfkit

input_filename = 'template.html'
output_filename = 'template.pdf'

with open(input_filename, 'r') as f:
    html_text = f.read()

pdfkit.from_string(html_text, output_filename)

# Use False instead of output path to save pdf to a variable
# pdf = pdfkit.from_url('http://google.com', False)
