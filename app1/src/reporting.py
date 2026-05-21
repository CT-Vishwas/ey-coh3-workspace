# generate a code Function to generate a report in pdf format using the reportlab library
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
def generate_report(data, file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, "Compliance Report")
    c.drawString(100, height - 120, f"Total Applications: {data['Total Applications']}")
    c.drawString(100, height - 140, f"Compliant Applications: {data['Compliant Applications']}")
    c.drawString(100, height - 160, f"Non-Compliant Applications: {data['Non-Compliant Applications']}")
    # add the compliance status pie chart to the report
    c.drawImage('./output/compliance_status_pie_chart.png', 100, height - 400, width=400, height=300)
    
    c.save()