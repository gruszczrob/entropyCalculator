import sys
from collections import Counter
import math
from datetime import datetime

def calculate_entropy(float_values):
    """Calculate the entropy of the provided list of float values."""
    frequency = Counter(float_values)
    total_values = len(float_values)
    entropy = -sum((count / total_values) * math.log2(count / total_values) for count in frequency.values())
    return entropy, total_values

def read_hex_values_from_file(filename):
    """Read hex values from a file and convert them to floats."""
    try:
        with open(filename, "r") as file:
            float_values = [float(int(line, 16)) for line in file if line.strip()]
        return float_values
    except FileNotFoundError:
        print(f"Could not open the file {filename}")
        sys.exit(1)

def get_current_date_time():
    """Get the current date and time as a string."""
    return datetime.now().strftime("%Y-%m-%d,%H:%M:%S")

def write_to_file(filename, original_filename, seeds_number, entropy):
    """Write the entropy and other details to a file."""
    try:
        # Check if file exists and if not, write the header
        file_exists = False
        try:
            with open(filename, "r") as file:
                file_exists = True
        except FileNotFoundError:
            pass

        with open(filename, "a") as file:
            if not file_exists:
                file.write("Date,Time,FileName,SeedsNumber,Entropy\n")
            
            current_date_time = get_current_date_time()
            file.write(f"{current_date_time},{original_filename},{seeds_number},{entropy}\n")
    
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <inputFilename> ")
        sys.exit(1)

    input_filename = sys.argv[1]
    

    # Read hex values and calculate entropy
    float_values = read_hex_values_from_file(input_filename)
    if float_values:
        entropy, total_values = calculate_entropy(float_values)
        print(f"Entropy: {entropy}")

        # Write the results to the output file
        if len(sys.argv) > 2:
            output_filename = sys.argv[2]
            write_to_file(output_filename, input_filename, total_values, entropy)
    else:
        print("The file contains no data.")
        sys.exit(1)

if __name__ == "__main__":
    main()

