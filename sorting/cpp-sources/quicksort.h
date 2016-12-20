#ifndef QUICKSORT_H_INCLUDED
#define QUICKSORT_H_INCLUDED

#include <vector>
#include <iostream>
#include <vector>
#include <ctime>

#include "declaration.h"

algorithmPerformance quicksort(std::vector<double>);
algorithmPerformance quicksort(std::vector<date>);

template <typename T>
void quicksort_algorithm(std::vector<T> &vector,
                         int left,
                         int right,
                         int cmpFn(T, T),
                         algorithmPerformance &perfomance) {
    int i = left;
    int j = right;
    T pivot = vector[(i + j) / 2];
    perfomance.ovh += 3; // initialize variables

    perfomance.ovh++; // test `while` condition first time
    while (i <= j) {
        perfomance.cmp++; // compare elements first time
        while (cmpFn(vector[i], pivot) == -1) {
            perfomance.cmp++; // compare elements
            i++;
            perfomance.ovh++; // increase variable
        }

        perfomance.cmp++; // compare elements first time
        while (cmpFn(vector[j], pivot) == 1) {
            perfomance.cmp++; // compare elements
            j--;
            perfomance.ovh++; // decrease variable
        }

        perfomance.ovh++; // test `if` condition
        if (i <= j) {
            swap(vector, i, j);
            perfomance.mov += 3; // swap elements

            i++;
            j--;
            perfomance.ovh += 2; // decrease vars
        }

        perfomance.ovh++; // test `while` finish condition
    }

    perfomance.ovh++; // test `if` condition
    if (j > left) {
        quicksort_algorithm(vector, left, j, cmpFn, perfomance);
    }

    perfomance.ovh++; // test `if` condition
    if (i < right) {
        quicksort_algorithm(vector, i, right, cmpFn, perfomance);
    }
}

#endif // QUICKSORT_H_INCLUDED
