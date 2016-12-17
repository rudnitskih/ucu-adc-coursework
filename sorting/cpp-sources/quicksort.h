#ifndef QUICKSORT_H_INCLUDED
#define QUICKSORT_H_INCLUDED

#include <vector>
#include <iostream>
#include <vector>
#include <ctime>

#include "declaration.h"

void quicksort(std::vector<double>);
void quicksort(std::vector<date>);

template <typename T>
void quicksort_algorithm(std::vector<T> &vector,
                         int left,
                         int right,
                         int cmpFn(T, T)) {
    int i = left;
    int j = right;
    T pivot = vector[(i + j) / 2];

    while (i <= j) {
        while (cmpFn(vector[i], pivot) == -1)
            i++;
        while (cmpFn(vector[j], pivot) == 1)
            j--;
        if (i <= j) {
            swap(vector, i, j);
            i++;
            j--;
        }
    }

    if (j > left) {
        quicksort_algorithm(vector, left, j, cmpFn);
    }

    if (i < right) {
        quicksort_algorithm(vector, i, right, cmpFn);
    }
}

#endif // QUICKSORT_H_INCLUDED
