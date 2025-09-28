import csv
import pandas as pd

rows = []
with open('./outputs/Lecture1_Glossary.csv', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)  # standard csv handles weird quoting better than pandas directly
    for i, row in enumerate(reader):
        # Skip empty lines
        if not row or all(cell.strip() == '' for cell in row):
            continue
        # Skip code fence lines (```csv)
        if row[0].strip().startswith('```'):
            continue

        # If more than 4 columns, merge columns 4..end into last col
        if len(row) > 4:
            row = row[:3] + [','.join(row[3:])]

        # If less than 4 columns, pad with empty strings
        while len(row) < 4:
            row.append('')

        rows.append(row)

# First row is header, rest are data
header = rows[0]
data = rows[1:]

# Build DataFrame
df = pd.DataFrame(data, columns=header)

# Ensure column names are exactly what you want
df.columns = [
    'Term',
    'Plain-English Explanation',
    'Prerequisite Material Location',
    'How Used in ML & Deep Learning'
]

# Save cleaned CSV
df.to_csv('./outputs/Lecture1_Glossary_fixed.csv', index=False)
print("Cleaned CSV saved to ./outputs/Lecture1_Glossary_fixed.csv")
