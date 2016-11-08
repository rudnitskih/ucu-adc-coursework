#include <iostream>
#include <cstdlib>
#include <fstream>

void datesGenerator() {
    std::ofstream datesFile;
    datesFile.open("../data/dates");

    srand((unsigned)time(NULL));

    for (int i = 0; i < 10000; i++ ){
        int year = rand() % 20 + 1996;
        int month = rand() % 12 + 1;
        int day = rand() % 28 + 1;

        datesFile << day << "/" << month << "/" << year << std::endl ;
    }

    datesFile.close();
}
