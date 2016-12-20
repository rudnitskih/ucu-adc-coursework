#include <iostream>
#include <fstream>

#include "declaration.h"
#include "quicksort.h"
#include "heapsort.h"

#define REALS                 1  // 2^0, bit 0
#define DATES                 2  // 2^1, bit 1
#define QUICKSORT             4  // 2^2, bit 2
#define HEAPSORT              8  // 2^3, bit 3

void addPerfomanceValues(algorithmPerformance &perfomance, algorithmPerformance &currentPerfomance) {
    perfomance.cmp += currentPerfomance.cmp;
    perfomance.mov += currentPerfomance.mov;
    perfomance.ovh += currentPerfomance.ovh;
    perfomance.time += currentPerfomance.time;
}

void initPerfomanceValues(algorithmPerformance &perfomance) {
    perfomance.cmp = 0;
    perfomance.mov = 0;
    perfomance.ovh = 0;
    perfomance.time = 0;
}

void calculateAvaragePerfomance(algorithmPerformance &perfomance, int valuesLength) {
    perfomance.cmp /= valuesLength;
    perfomance.mov /= valuesLength;
    perfomance.ovh /= valuesLength;
    perfomance.time /= valuesLength;
}

void choseSortProcesses(unsigned char flags, unsigned int n = 10) {
    std::vector<double> reals;
    std::vector<date> dates;

    if ((flags & REALS) == REALS) {
         generator(n, reals);
    }

    if ((flags & DATES) == DATES) {
         generator(n, dates);
    }

    if ((flags & QUICKSORT) == QUICKSORT) {
        if ((flags & REALS) == REALS) {
             runSortProcess(reals, "quicksort");
        }

        if ((flags & DATES) == DATES) {
             runSortProcess(dates, "quicksort");
        }
    }

    if ((flags & HEAPSORT) == HEAPSORT) {
        if ((flags & REALS) == REALS) {
            runSortProcess(reals, "heapsort");
        }

        if ((flags & DATES) == DATES) {
            runSortProcess(dates, "heapsort");
        }
    }
}

int getFlags(int dataType, int algorithm) {
    unsigned char flags = 0;

    switch (dataType) {
        case 1:
            flags |= REALS;
            break;

        case 2:
            flags |= DATES;
            break;

        default:
            flags |= REALS;
            flags |= DATES;
    }

    switch (algorithm) {
        case 1:
            flags |= QUICKSORT;
            break;

        case 2:
            flags |= HEAPSORT;
            break;

        default:
            flags |= QUICKSORT;
            flags |= HEAPSORT;
    }

    return flags;
}

std::vector<unsigned int> getSortVectorsSizes(unsigned int min,
                                              unsigned int max,
                                              unsigned int points) {
    std::vector<unsigned int> sizes;
    unsigned int difference = (max - min) / (points - 1);

    for (unsigned int i = 0; i < points; i++) {
        sizes.push_back(min + i*difference);
    }

    return sizes;
}

int main() {
    int dataType;
    int algorithm;
    int mode;
    unsigned char flags;

    std::ofstream ofs;
    system("exec find ../program-results -type f -name '*.csv' -delete");

    std::cout << "Choose data:\n 1 - Reals \n 2 - Dates \n 3 - Both \n";
    std::cin >> dataType;

    std::cout << "Choose algorithm:\n 1 - Quicksort \n 2 - Heapsort \n 3 - Both \n";
    std::cin >> algorithm;

    std::cout << "Mode:\n 1 - Development \n 2 - Production \n";
    std::cin >> mode;

    flags = getFlags(dataType, algorithm);

    if (mode == 1) {
        choseSortProcesses(flags);
    } else {
        std::vector<unsigned int> sizes = getSortVectorsSizes(10000, 300000, 30);

        for(std::vector<unsigned int>::iterator it = sizes.begin();
            it != sizes.end();
            ++it) {
            choseSortProcesses(flags, *it);
        }
    }

   return 0;
}
