import pandas as pd

# Load the Excel file
file_path = "payroll_data.xlsx"
df = pd.read_excel(file_path)

# Calculate Gross Salary (Hours Worked * Hourly Rate)
df["Gross Salary"] = df["Hours Worked"] * df["Hourly Rate"]

# Calculate Tax Deduction
df["Tax Deduction"] = (df["Tax %"] / 100) * df["Gross Salary"]

# Calculate Net Salary
df["Net Salary"] = df["Gross Salary"] - df["Tax Deduction"]

# Save the updated data back to Excel
output_file = "updated_payroll.xlsx"
df.to_excel(output_file, index=False)

print(f"Updated payroll data saved to {output_file}")


