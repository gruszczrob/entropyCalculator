import sys
from collections import Counter
import math

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        # Read the content of the file
        with open(filename, "r") as file:
            hex_values = file.read().splitlines()

        # Convert hex values to float
        float_values = [float(int(value, 16)) for value in hex_values]

        # Calculate the frequency of each value
        frequency = Counter(float_values)

        # Calculate the total number of values
        total_values = len(float_values)

        # Calculate the entropy
        entropy = -sum((count / total_values) * math.log2(count / total_values) for count in frequency.values())

        # Print the entropy
        print(f"Entropy: {entropy}")

    except FileNotFoundError:
        print(f"Could not open the file {filename}")
        sys.exit(1)

if __name__ == "__main__":
    main()

