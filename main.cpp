#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>
#include <unordered_map>

// Funkcja do obliczania entropii
double countEntropy(const std::vector<double>& array) {
    std::unordered_map<double, int> frequency;
    
    for (const auto& value : array) {
        frequency[value]++;
    }

    // Obliczenie entropii
    double entropy = 0.0;
    double totalElements = array.size();
    
    for (const auto& [value, count] : frequency) {
        double probability = count / totalElements;
        entropy -= probability * std::log2(probability);
    }
    
    return entropy;
}

// Funkcja do odczytu danych z pliku
std::vector<double> readHexArrayFromFile(const std::string& filename) {
    std::vector<double> array;
    std::ifstream file(filename);

    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            std::stringstream ss;
            ss << std::hex << line;
            unsigned int value;
            ss >> value;
            array.push_back(static_cast<double>(value));
        }
        file.close();
    } else {
        std::cerr << "Nie można otworzyć pliku: " << filename << std::endl;
    }

    return array;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <filename>" << std::endl;
        return 1;
    }

    std::string filename = argv[1];
    std::vector<double> data = readHexArrayFromFile(filename);
    
    if (!data.empty()) {
        double entropy = countEntropy(data);
        std::cout << "Entropia: " << entropy << std::endl;
    } else {
        std::cout << "Plik nie zawiera żadnych danych." << std::endl;
    }

    return 0;
}

