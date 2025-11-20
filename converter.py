import pandas as pd

# Path to your .ods file
ods_file = "info.ods"

# Sheet name you want to convert (default is first sheet)
sheet_name = 0  # you can also use sheet name as string, e.g., "Sheet1"

# Read the .ods file
df = pd.read_excel(ods_file, engine="odf", sheet_name=sheet_name)

# Path for the output CSV
csv_file = "output.csv"

# Save as CSV
df.to_csv(csv_file, index=False)

print(f"Converted '{ods_file}' to '{csv_file}' successfully!")