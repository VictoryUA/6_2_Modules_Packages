import csv
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

def convert_temperature(temperature, target_unit):
    """
    Converts the temperature to the target unit
    """
    if target_unit == 'F':
        return celsius_to_fahrenheit(temperature)
    elif target_unit == 'C':
        return fahrenheit_to_celsius(temperature)
    else:
        raise ValueError("Invalid target temperature unit")

def main(input_file, output_file, target_unit):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip title
        rows = list(reader)

    converted_rows = []
    for row in rows:
        date, distance, temperature = row
        temperature = float(temperature.rstrip('°C').rstrip('°F'))  # Remove degree symbols and convert to a number
        converted_temperature = convert_temperature(temperature, target_unit)
        converted_rows.append([date, distance, f"{converted_temperature}°{target_unit}"])

    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Distance', 'Converted Temperature'])
        writer.writerows(converted_rows)

if __name__ == "__main__":
    input_file = 'data.csv'
    output_file = 'converted_data.csv'
    target_unit = 'F'  # Може бути 'F' або 'C'
    main(input_file, output_file, target_unit)