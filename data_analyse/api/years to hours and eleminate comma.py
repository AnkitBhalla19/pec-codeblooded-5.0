
input_file = '2017.csv'
output_file = 'output4.csv'


columns_to_keep = ['WAGE_RATE_OF_PAY_FROM', 'WAGE_UNIT_OF_PAY']
conversion_rates = {
    'Year': 1,
    'Month': 12,
    'Hour': 8760,
    'Week': 52,
    'Bi-Weekly': 26
}
unit_conversions = {
    'Year': 'year',
    'Month': 'year',
    'Hour': 'year',
    'Week': 'year',
    'Bi-Weekly': 'year'
}

# Open the input and output files
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    # Import the CSV reader and writer
    import csv

    # Create CSV reader and writer objects
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header row to get the column names and their indices
    header = next(reader)
    header_indices = {header[i]: i for i in range(len(header))}

    # Determine the indices of the columns to keep
    wage_column_index = header_indices['WAGE_RATE_OF_PAY_FROM']
    unit_column_index = header_indices['WAGE_UNIT_OF_PAY']

    # Write the header row with the selected columns to the output CSV
    writer.writerow(columns_to_keep)

    # Process each row in the input CSV, convert salary, and change unit names
    for row in reader:
        wage_str = row[wage_column_index]
        unit = row[unit_column_index]

        # Remove commas and convert the wage to float
        wage_str = wage_str.replace(',', '')

        if unit in conversion_rates:
            wage = float(wage_str) * conversion_rates[unit]
            # Update the 'WAGE_RATE_OF_PAY_FROM' column with the converted value
            row[wage_column_index] = wage
            # Update the 'WAGE_UNIT_OF_PAY' column with the converted unit name
            row[unit_column_index] = unit_conversions[unit]

        # Write the updated row to the output CSV
        writer.writerow([row[wage_column_index], row[unit_column_index]])

print("Salaries converted and saved to", output_file)
