#include <iostream>
#include <vector>

#include "declaration.h"

void generator(long n, std::vector<double>& reals) {
    srand((unsigned)time(NULL));

    for (long i = 0; i < n; i++ ){
        double r = ((double)rand() / (double)(RAND_MAX));
        reals.push_back(r);
    }
}

void generator(long n, std::vector<date>& dates) {
    srand((unsigned)time(NULL));
    date date;

    for (long i = 0; i < n; i++ ){
        date.year = rand() % 20 + 1996;
        date.month = rand() % 12 + 1;
        date.day = rand() % 28 + 1;

        dates.push_back(date);
    }
}
