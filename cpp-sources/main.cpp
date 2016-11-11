#include <iostream>
#include "generator.h"
#include "sorter.h"

void generator() {
    int type;

    std::cout << "Type of data:\n 1 - Reals \n 2 - Dates \n Your chose:  ";
    std::cin >> type;

    switch (type) {
        case 1:
            realsGenerator();

            break;
        case 2:
            datesGenerator();

            break;

        default:
            std::cout << "Not correct value";
    }

}

int main() {
   int operation;
   bool did = true;

   std::cout << "Choose function:\n 1 - Generator \n 2 - Sorting \n";

   do {
       std::cin >> operation;

       switch (operation) {
            case 1:
                generator();

                break;
            case 2:
                sortData();
                break;

            default:
                did = false;

        }
        did;
   } while (!did);

   return 0;
}
