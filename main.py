import sys
from collections import Counter
import math
from datetime import datetime
import argparse

def calculate_entropy(values):
    """Calculate the entropy of the provided list of values."""
    frequency = Counter(values)
    total_values = len(values)
    entropy = -sum((count / total_values) * math.log2(count / total_values) for count in frequency.values())
    return entropy, total_values


def calculate_entropies(values, data_len):
    """Calculate entropy for all possible substrings from length 1 to data_len."""
    entropies = []
    for length in range(1, data_len+1):  # Lengths from 1 to data_len+1
        for start in range(data_len - length + 1):  # Possible starting points for substrings
            substrings = [value[start:start + length] for value in values]
            entropy, _ = calculate_entropy(substrings)
            positions = ";".join(str(i) for i in range(start, start + length))
            entropies.append((positions, entropy))
    return entropies


def read_values_from_file(filename):
    """Read values from a file."""
    try:
        with open(filename, "r") as file:
            values = [line.strip() for line in file if line.strip()]
        return values
    except FileNotFoundError:
        print(f"Could not open the file {filename}")
        sys.exit(1)


def read_unique_values_from_file(filename):
    """Read values from a file, treating consecutive identical seeds as one."""
    try:
        with open(filename, "r") as file:
            unique_values = []
            previous_value = None
            for line in file:
                current_value = line.strip()
                if current_value != previous_value:
                    unique_values.append(current_value)
                previous_value = current_value
        return unique_values
    except FileNotFoundError:
        print(f"Could not open the file {filename}")
        sys.exit(1)


def get_current_date_time():
    """Get the current date and time as a string."""
    return datetime.now().strftime("%Y-%m-%d,%H:%M:%S")


def write_to_file(filename, original_filename, seeds_number, if_merge, entropies):
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
                file.write("Date,Time,FileName,SeedsNumber,Postion,IfMerge,Entropy\n")
            for positions, entropy in entropies:
                current_date_time = get_current_date_time()
                file.write(f"{current_date_time},{original_filename},{seeds_number},{positions},{if_merge},{entropy}\n")
    
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Calculate entropy of values from a file.")
    parser.add_argument("input_filename", type=str, help="Name of the file to read values from")
    parser.add_argument("-o", "--output_filename", type=str, help="Optional file to save results")
    parser.add_argument("-u", "--unique", action="store_true", help="Treat consecutive identical seeds as one")
    parser.add_argument("-c", "--calculate_all", type=int, help="Calculate entropy for all possible substrings")
    
    args = parser.parse_args()
    if args.unique:
        values = read_unique_values_from_file(args.input_filename)
    else:
        values = read_values_from_file(args.input_filename)

    if args.calculate_all:
        if not all(len(value) == args.calculate_all for value in values):
            print(f"All values must be exactly {args.calculate_all} characters long for substring calculations.")
            sys.exit(1)
        entropies = calculate_entropies(values, args.calculate_all)
        if args.output_filename:
            write_to_file(args.output_filename, args.input_filename, len(values), args.unique, entropies)
        else:
            for positions, entropy in entropies:
                print(f"Positions: {positions}, Entropy: {entropy}")
    else:
        if values:
            entropy, total_values = calculate_entropy(values)
            print(f"Entropy: {entropy}")
            # Write the results to the output file
            if args.output_filename:
                write_to_file(args.output_filename, args.input_filename, len(values), args.unique, [("all", entropy)])
        else:
            print("The file contains no data.")
            sys.exit(1)


if __name__ == "__main__":
    main()

