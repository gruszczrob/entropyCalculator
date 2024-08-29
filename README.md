# Entropy Calculator

<p align="center">
  <img src="https://github.com/user-attachments/assets/c3feb796-f6c6-4b30-befd-95c9b8f09255" alt="Image" height="200">
</p>

**Entropy Calculator** is an open-source tool designed to calculate the entropy of data stored in a file. This project is implemented in both Python and C++, providing flexibility and convenience for users who prefer either language. The program is ready to use immediately after compiling (for the C++ version) or executing (for the Python version) and is designed to be simple yet efficient.

The Python version currently offers more advanced functionality, such as calculating entropy for all possible substrings and handling unique value sequences. The C++ version is under active development and will gradually incorporate these advanced features.

## Table of Contents

- [What is Entropy?](#what-is-entropy)
  - [Entropy Calculation](#entropy-calculation)
- [System Requirements](#system-requirements)
- [Installation and Usage](#installation-and-usage)
  - [C++ Version](#c-version)
  - [Python Version](#python-version)
- [Example Usage](#example-usage)
- [Saving Results to CSV](#saving-results-to-csv)
- [License](#license)
- [Contributing](#contributing)
- [Author](#author)
- [Contact](#contact)

## What is Entropy?

Entropy, in the context of information theory, is a measure of the uncertainty or randomness in a dataset. Introduced by Claude Shannon in 1948, entropy quantifies the amount of information contained in a message or, more generally, in any dataset. It is a fundamental concept in fields such as cryptography, data compression, and statistical mechanics.

In simpler terms, if the content of a dataset is highly predictable (e.g., all entries are the same), the entropy is low. Conversely, if the dataset is highly unpredictable (e.g., all entries are unique or randomly distributed), the entropy is high. Entropy provides insight into the complexity and randomness of the data, which is particularly useful when evaluating the strength of cryptographic keys or the efficiency of data compression algorithms.




### Entropy Calculation

The entropy \( H(X) \) of a random variable \( X \) with a set of possible outcomes \( \{x_1, x_2, ..., x_n\} \) and corresponding probabilities \( \{p_1, p_2, ..., p_n\} \) is calculated using the following formula:

\[
H(X) = -\sum_{i=1}^{n} p(x_i) \log_2 p(x_i)
\]

Where:
- \( p(x_i) \) is the probability of occurrence of the outcome \( x_i \).
- \( \log_2 \) is the logarithm to the base 2.

#### Steps to Calculate Entropy:

1. **Determine the Probability Distribution:**
   - Identify all unique symbols or values in the dataset.
   - Calculate the probability \( p(x_i) \) of each unique symbol. This is done by dividing the frequency of each symbol by the total number of symbols in the dataset.

2. **Calculate the Entropy:**
   - For each unique symbol \( x_i \), compute \( p(x_i) \log_2 p(x_i) \).
   - Sum all the values obtained in the previous step.
   - Multiply the sum by \(-1\) to obtain the entropy \( H(X) \).
  
<p align="center">
  <img src="https://github.com/user-attachments/assets/dd6b74b5-dc47-41f6-a451-a840f77cf01d" alt="Image" height="200">
</p>

The result is the entropy value, which quantifies the average amount of information (in bits) produced by the dataset. A higher entropy value indicates greater randomness and unpredictability, whereas a lower value indicates more regularity and predictability in the dataset.

## System Requirements

### Python Version

- **Python:** Version 3 or higher

### C++ Version

- **Compiler:** Any compiler that supports C++17 (the project has been tested with GCC and Clang++)

The Python version requires no additional libraries outside of the standard Python distribution, making it highly portable and easy to set up. The C++ version, due to its use of modern C++ features, requires a compiler that is compliant with the C++17 standard.

## Installation and Usage

### C++ Version

To use the C++ version of Entropy Calculator, follow these steps:

1. **Compile the Program:**

   Open your terminal and navigate to the directory containing `main.cpp`, then run the following command:

   ```bash
   g++ -std=c++17 -o main main.cpp
   ```

   This will produce an executable named `main`.

2. **Run the Program:**

   After compiling, you can run the program by specifying the path to your data file as an argument:

   ```bash
   ./main [FILE NAME]
   ```

   Replace `[FILE NAME]` with the actual name of your file containing data.

### Python Version

To use the Python version, ensure you have Python 3 installed on your system. Then, you can directly run the script as follows:

```bash
python3 main.py [FILE NAME]
```

Again, replace `[FILE NAME]` with the actual path to your data file.

### Advanced Usage Options (Python Version Only)

The Python version of the Entropy Calculator offers several advanced features:

- **Unique Sequence Handling:**
  To treat consecutive identical entries in the data file as a single entry, use the `-u` or `--unique` flag.

  ```bash
  python3 main.py [FILE NAME] -u
  ```

- **Entropy Calculation for All Possible Substrings:**
  To calculate the entropy for all possible substrings of a specified length, use the `-c` or `--calculate_all` option followed by the desired substring length.

  ```bash
  python3 main.py [FILE NAME] -c [LENGTH]
  ```

- **Saving Results to a File:**
  To save the results of the entropy calculations to a CSV file, specify the output filename using the `-o` or `--output_filename` option.

  ```bash
  python3 main.py [FILE NAME] -o [OUTPUT FILE]
  ```

These features make the Python version particularly powerful for complex data analysis tasks.

Sekcję o formacie pliku wejściowego najlepiej dodać przed sekcją [Example Usage](#example-usage) w pliku README. Poniżej znajduje się treść tej sekcji:

## Input File Format

The input file for the Entropy Calculator should contain data entries separated by line breaks. Each line in the file is treated as a separate data value. The tool is flexible and can process various types of data, including:

- **Hexadecimal Numbers:** e.g., `A1`, `FF`, `0C`
- **Text Strings:** e.g., `HelloWorld`, `TestData`
- **Numeric Values:** e.g., `12345`, `67890`
- **Special Characters:** e.g., `!@#$`, `%^&*`

**Note:** The program removes any leading or trailing whitespace from each line before processing. Empty lines are ignored.

### Example of a Valid Input File

```
A1
FF
HelloWorld
12345
!@#$
```

Each line represents a separate data entry that will be included in the entropy calculation. The order and format of the entries can influence the calculated entropy, especially when using advanced options such as unique sequence handling or substring entropy calculations.

## Example Usage

Suppose you have a file named `data.txt` containing various data entries like this:

```
A1
FF
HelloWorld
12345
!@#$
```

You can calculate the entropy by running the following commands:

### C++ Version

```bash
./main data.txt
```

### Python Version

```bash
python3 main.py data.txt
```

The program will read the `data.txt` file, compute the entropy, and display the result in the terminal. The output might look something like:

```
Entropy: 2.321928094887362
```

This value represents the amount of randomness or uncertainty in the dataset.

### Advanced Example (Python Version)

To calculate entropy for all possible substrings of length 3 and save the results to a file named `results.csv`:

```bash
python3 main.py data.txt -c 3 -o results.csv
```

The program will analyze the substrings, calculate their respective entropies, and save the output in the specified CSV file.

## Saving Results to CSV

The Entropy Calculator offers the option to save the computed entropy to a CSV file. This can be particularly useful for keeping a record of entropy calculations across multiple files, which can be useful for batch processing or historical analysis.

### C++ Version

```bash
./main data.txt output.csv
```

### Python Version

```bash
python3 main.py data.txt -o output.csv
```

The CSV file will be formatted as follows:

```csv
Date,Time,FileName,SeedsNumber,Position,IfMerge,Entropy
2024-08-27,13:22:00,data.txt,5,all,FALSE,Entropy: 2.321928094887362
```

Each row in the CSV file represents an entropy calculation, with details such as the date, time, file name, and specific substring positions.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software, provided that you include the original license file in any distribution. For more detailed information, please refer to the `LICENSE` file included in the repository.

## Contributing

Contributions to the Entropy Calculator project are welcome! If you find a bug, have a feature request, or want to improve the code, feel free to open an issue or submit a pull request. Please ensure that your contributions align with the project’s goals and that you follow the coding standards outlined in the repository.

**Note:** The C++ version is currently under active development and will gradually incorporate the advanced features already available in the Python version. Contributions to both versions are appreciated.

## Author

This project was developed by [Robert Gruszczyński](https://github.com/gruszczrob). I am passionate about developing tools that help others better understand and analyze data.

## Contact

If you have any questions, suggestions, or feedback regarding the Entropy Calculator, please feel free to reach out to me via email at [gruszczrobert@proton.me](mailto:gruszczrobert@proton.me). I appreciate all forms of feedback and am always looking to improve the project.
