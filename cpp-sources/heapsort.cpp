#include <iostream>
#include <vector>
#include <ctime>

#include "declaration.h"
#include "heapsort.h"

void heapsort(std::vector<double> vector) {
    std::clock_t begin = std::clock();

    heapsort_algorithm(vector, cmp);

    std::clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    std::cout << "TIME(sec): " << elapsed_secs << std::endl << std::endl;
}

void heapsort(std::vector<date> vector) {
    std::clock_t begin = std::clock();

    heapsort_algorithm(vector, compare_dates);

    std::clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    std::cout << "TIME(sec): " << elapsed_secs << std::endl << std::endl;
}
