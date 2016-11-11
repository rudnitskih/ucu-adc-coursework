#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>

void quickSort(std::vector<double>&);

void sortData() {
    int dataType = 0;
    bool chosed = true;
    int n = 0;
    std::string line;
    std::vector<double> reals;
    std::string temp;

    std::cout << "Choose data:\n 1 - Reals \n 2 - Dates \n";

    std::ifstream realsFile("../data/reals");

    while (getline(realsFile, temp)) {
        reals.push_back(std::stod(temp));
    }

    realsFile.close();

    // int array[] = {95, 45, 48, 98, 1, 485, 65, 478, 1, 2325};

    quickSort(reals);

    //std::cout << reals[0] << ":::" << reals[9998];

    //std::cin >> dataType;
}
