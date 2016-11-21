#ifndef QUICKSORT_H_INCLUDED
#define QUICKSORT_H_INCLUDED

#include <vector>
#include "declaration.h"

void quicksort(std::vector<double>&);
void quicksort(std::vector<date>&);

template <typename T>
void quicksort_algorithm(std::vector<T> &array, int left, int right, int cmpFn(T, T)) {
    int i = left;
    int j = right;
    T pivot = array[(i + j) / 2];

    while (i <= j) {
        while (cmpFn(array[i], pivot) == -1)
            i++;
        while (cmpFn(array[j], pivot) == 1)
            j--;
        if (i <= j) {
            swap(array, i, j);
            i++;
            j--;
        }
    }

    if (j > left) {
        quicksort_algorithm(array, left, j, cmpFn);
    }

    if (i < right) {
        quicksort_algorithm(array, i, right, cmpFn);
    }
}

#endif // QUICKSORT_H_INCLUDED
