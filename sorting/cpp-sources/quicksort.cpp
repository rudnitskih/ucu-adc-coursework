#include <iostream>
#include <vector>
#include <ctime>

#include "declaration.h"
#include "quicksort.h"

algorithmPerformance quicksort(std::vector<date> vectorWithData) {
    algorithmPerformance perfomance;

    std::clock_t begin = std::clock();
    quicksort_algorithm(vectorWithData, 0, vectorWithData.size() - 1, compare_dates, perfomance);
    std::clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    std::cout << "TIME(sec): " << elapsed_secs << std::endl << std::endl;

    perfomance.time = elapsed_secs;

    return perfomance;
}

algorithmPerformance quicksort(std::vector<double> vectorWithData) {
    algorithmPerformance perfomance;

    std::clock_t begin = std::clock();
    quicksort_algorithm(vectorWithData, 0, vectorWithData.size() - 1, cmp, perfomance);
    std::clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    std::cout << "TIME(sec): " << elapsed_secs << std::endl << std::endl;

    perfomance.time = elapsed_secs;

    return perfomance;
}
