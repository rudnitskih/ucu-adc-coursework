#include <iostream>
#include "generator.h"

int main() {
   int operation;
   bool did = true;

   std::cout << "Choose function:\n 1 - Generator \n 2 - Sorting \n";

   do {
       std::cin >> operation;

       switch (operation) {
            case 1:
                datesGenerator();

                break;
            case 2:
                break;

            default:
                did = false;

        }
        did;
   } while (!did);

   return 0;
}
