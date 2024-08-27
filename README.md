# Entropy Calculator

<p align="center">
  <img src="https://github.com/user-attachments/assets/c3feb796-f6c6-4b30-befd-95c9b8f09255" alt="Image" height="200">
</p>


**Entropy Calculator** is an open-source tool designed to calculate the entropy of hexadecimal data stored in a file. This project is implemented in both Python and C++, providing flexibility and convenience for users who prefer either language. The program is ready to use immediately after compiling (for the C++ version) or executing (for the Python version) and is designed to be simple yet efficient.

## Table of Contents

- [How It Works](#how-it-works)
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

## How It Works

The Entropy Calculator processes a file containing hexadecimal numbers, where each number is expected to be on a separate line. The program reads these numbers, computes the entropy based on the probability distribution of the different hex values, and then displays the entropy value directly in the terminal. Additionally, the tool provides an option to save the computed entropy to a CSV file, which can be useful for further data analysis or record-keeping.

This tool is particularly useful for analyzing the randomness or information content of data, which can be crucial in fields such as cryptography, data compression, and information theory.

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

   Replace `[FILE NAME]` with the actual name of your file containing hexadecimal data.

### Python Version

To use the Python version, ensure you have Python 3 installed on your system. Then, you can directly run the script as follows:

```bash
python3 main.py [FILE NAME]
```

Again, replace `[FILE NAME]` with the actual path to your data file.

## Example Usage

Suppose you have a file named `data.txt` containing hexadecimal numbers like this:

```
A1
FF
0C
B3
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
Entropy: 3.459
```

This value represents the amount of randomness or uncertainty in the dataset.

## Saving Results to CSV

The Entropy Calculator also offers the option to save the computed entropy to a CSV file. To do this, provide an additional argument when running the program, specifying the name of the CSV file where the results should be saved.

### C++ Version

```bash
./main data.txt output.csv
```

### Python Version

```bash
python3 main.py data.txt output.csv
```

In this example, the entropy will be calculated and saved in `output.csv` in the following format:

```csv
Date,Time,FileName,SeedsNumber,Entropy
2024-08-27,13:22:00,data.txt,3.459
```

This allows you to keep a record of entropy calculations across multiple files, which can be particularly useful for batch processing or historical analysis.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software, provided that you include the original license file in any distribution. For more detailed information, please refer to the `LICENSE` file included in the repository.

## Contributing

Contributions to the Entropy Calculator project are welcome! If you find a bug, have a feature request, or want to improve the code, feel free to open an issue or submit a pull request. Please ensure that your contributions align with the project’s goals and that you follow the coding standards outlined in the repository.

## Author

This project was developed by [Robert Gruszczyński](https://github.com/gruszczrob). I am passionate about developing tools that help others better understand and analyze data.

## Contact

If you have any questions, suggestions, or feedback regarding the Entropy Calculator, please feel free to reach out to me via email at [gruszczrobert@proton.me](mailto:gruszczrobert@proton.me). I appreciate all forms of feedback and am always looking to improve the project.
