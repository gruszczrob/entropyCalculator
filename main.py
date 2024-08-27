import sys
from collections import Counter
import math

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as file:
            float_values = [float(int(line, 16)) for line in file if line.strip()]

        frequency = Counter(float_values)
        total_values = len(float_values)
        entropy = -sum((count / total_values) * math.log2(count / total_values) for count in frequency.values())

        print(f"Entropy: {entropy}")

    except FileNotFoundError:
        print(f"Could not open the file {sys.argv[1]}")
        sys.exit(1)

if __name__ == "__main__":
    main()

