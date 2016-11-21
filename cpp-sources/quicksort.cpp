#include <iostream>
#include <vector>
#include <ctime>

#include "declaration.h"
#include "quicksort.h"

void quicksort(std::vector<date> &array) {
    print_vector(array, 10);
    std::cout << "===========================\n";
    std::clock_t begin = std::clock();
    quicksort_algorithm(array, 0, array.size() - 1, compare_dates);
    std::clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    print_vector(array, 10);
    std::cout << elapsed_secs;
}

void quicksort(std::vector<double> &array) {
    print_vector(array, 10);
    std::cout << "===========================\n";
    std::clock_t begin = std::clock();
    quicksort_algorithm(array, 0, array.size() - 1, cmp);
    std::clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    print_vector(array, 10);
    std::cout << elapsed_secs;
}
