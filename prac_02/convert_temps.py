def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def convert_temps(input_filename, output_filename):
    """Read Fahrenheit values and write Celsius values to output file."""
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            fahrenheit = float(line.strip())  # Read each temperature
            celsius = fahrenheit_to_celsius(fahrenheit)  # Convert to Celsius
            outfile.write(f"{celsius}\n")  # Write the converted temperature

if __name__ == "__main__":
    convert_temps('temps_input.txt', 'temps_output.txt')
    print("temps_output.txt has been created with converted temperatures.")
