from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
import pandas as pd

# Load payroll data
excel_file = "payroll_data.xlsx"  # Ensure this file exists
df = pd.read_excel(excel_file)

# Calculate Gross Salary and Net Salary
df["Gross Salary"] = df["Hours Worked"] * df["Hourly Rate"]
df["Net Salary"] = df["Gross Salary"] * (1 - df["Tax %"] / 100)

# Define PDF file name
pdf_file = "payroll_report.pdf"

# Create a PDF (landscape for more space)
c = canvas.Canvas(pdf_file, pagesize=landscape(letter))
c.setFont("Helvetica-Bold", 14)
c.drawString(250, 550, "Employee Payroll Report")

# Extract headers and dynamically adjust column spacing
headers = list(df.columns)
num_columns = len(headers)
page_width = 800  # Adjusted for landscape mode
column_width = page_width // (num_columns + 1)
x_positions = [50 + (i * column_width) for i in range(num_columns)]

# Set initial position
y_position = 500  

# Draw headers
c.setFont("Helvetica-Bold", 10)
for i, header in enumerate(headers):
    c.drawString(x_positions[i], y_position, str(header))

# Draw table rows
c.setFont("Helvetica", 10)
for _, row in df.iterrows():
    y_position -= 20
    for i, value in enumerate(row):
       c.drawString(x_positions[i], y_position, str(round(float(value), 2)) if isinstance(value, (int, float)) else str(value))


# Save the PDF
c.save()

print(f"Payroll report saved as {pdf_file}")


