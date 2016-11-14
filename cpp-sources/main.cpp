#include <iostream>
#include "declaration.h"

int main() {
    int dataType = 1;
    std::vector<double> reals;
    std::vector<date> dates;

    std::cout << "Choose data:\n 1 - Reals \n 2 - Dates \n";
    std::cin >> dataType;

    switch (dataType) {
        case 1: {
            generator(4, reals);
            quickSort(reals);
            break;
        }


        case 2: {
            generator(4, dates);
            quickSort(dates);


            break;
        }
    }

   return 0;
}
