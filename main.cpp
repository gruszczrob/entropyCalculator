#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>
#include <unordered_map>
#include <ctime>
#include <iomanip>

double totalElements;

// Function to calculate entropy
double calculateEntropy(const std::vector<double>& array) {
    std::unordered_map<double, int> frequencyMap;

    // Calculate frequency of each unique element in the array
    for (const auto& value : array) {
        frequencyMap[value]++;
    }

    // Calculate entropy
    double entropy = 0.0;
    totalElements = array.size();

    for (const auto& [value, count] : frequencyMap) {
        double probability = static_cast<double>(count) / totalElements;
        entropy -= probability * std::log2(probability);
    }

    return entropy;
}

// Function to read data from a file
std::vector<double> readHexArrayFromFile(const std::string& filename) {
    std::vector<double> array;
    std::ifstream file(filename);

    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            if (line.empty()) {
                continue;
            }
            std::stringstream ss;
            ss << std::hex << line;
            unsigned int value;
            ss >> value;
            array.push_back(static_cast<double>(value));
        }
        file.close();
    } else {
        std::cerr << "Cannot open file: " << filename << std::endl;
    }

    return array;
}

// Function to get the current date and time as a string
std::string getCurrentDateTime() {
    std::time_t now = std::time(nullptr);
    std::tm* localTime = std::localtime(&now);

    char buffer[100];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d,%H:%M:%S", localTime);

    return std::string(buffer);
}

// Function to write data to a file
void writeToFile(const std::string& filename, const std::string& fileToWriteName, int seedsNumber, double entropy) {
    std::ofstream file;

    // Check if file exists
    file.open(filename, std::ios::in);
    bool fileExists = file.good();
    file.close();

    // Open file in append mode
    file.open(filename, std::ios::app);

    if (!fileExists) {
        // If file doesn't exist, write the header
        file << "Date,Time,FileName,SeedsNumber,Entropy\n";
    }

    // Write the current date and time along with other data
    std::string currentDateTime = getCurrentDateTime();
    file << currentDateTime << "," << fileToWriteName << "," << seedsNumber << "," << entropy << "\n";

    file.close();
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <filename> " << std::endl;
        return 1;
    }

    std::string filename = argv[1];
    std::vector<double> data = readHexArrayFromFile(filename);

    if (!data.empty()) {
        double entropy = calculateEntropy(data);
        std::cout << "Entropy: " << entropy << std::endl;
        if(argc > 2){
	    std::string outputFilename = argv[2];
	    writeToFile(outputFilename, filename, static_cast<int>(totalElements), entropy);
	}
    } else {
        std::cout << "The file contains no data." << std::endl;
    }

    return 0;
}

