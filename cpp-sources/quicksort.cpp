#include <iostream>
#include <vector>
#include <ctime>
#include <functional>

#include "declaration.h"

void print_vector(std::vector<double> &array, unsigned n) {
    for (unsigned i = 0; i < n && i < array.size(); ++i)
        std::cout << array[i] << std::endl;
}

void print_vector(std::vector<date> &array, unsigned n) {
    for (unsigned i = 0; i < n && i < array.size(); ++i)
        std::cout << array[i].day << "/" << array[i].month << "/" << array[i].year << std::endl;
}

template <typename T1>
int cmp(T1 x, T1 y) {
    return (x>y) ? 1 : ((x<y) ? -1 : 0);
}

int compare_dates(date a, date b) {
    if (cmp(a.year, b.year) != 0)
        return cmp(a.year, b.year);

    if (cmp(a.month, b.month) != 0)
        return cmp(a.month, b.month);

    return cmp(a.day, b.day);
}

template <typename T>
void swap(std::vector<T>& vHeap, int i, int j) {
    if(i == j)
        return;

    T temp;
    temp = vHeap[i];
    vHeap[i] = vHeap[j];
    vHeap[j] = temp;
}

void algorithm(std::vector<double> &array, int left, int right, int cmpFn(double, double)) {
    int i = left;
    int j = right;
    double pivot = array[(i + j) / 2];

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
        algorithm(array, left, j, cmpFn);
    }

    if (i < right) {
        algorithm(array, i, right, cmpFn);
    }
}

void dates_algorithm(std::vector<date> &array, int left, int right, std::function<int (date, date)> cmp) {
    int i = left;
    int j = right;
    date pivot = array[(i + j) / 2];

    while (i <= j) {
        while (cmp(array[i], pivot) == -1) {
             i++;
            }

        while (cmp(array[j], pivot) == 1) {
            j--;
        }

        if (i <= j) {
            swap(array, i, j);
            i++;
            j--;
        }
    }

    if (j > left) {
        dates_algorithm(array, left, j, cmp);
    }

    if (i < right) {
        dates_algorithm(array, i, right, cmp);
    }
}

void quickSort(std::vector<double> &array) {
    print_vector(array, 10);
    std::cout << "===========================\n";
    algorithm(array, 0, array.size() - 1, cmp);
    print_vector(array, 10);
}

void quickSort(std::vector<date> &array) {
    print_vector(array, 10);
    std::cout << "===========================\n";
    std::clock_t begin = std::clock();
    dates_algorithm(array, 0, array.size() - 1, compare_dates);
    std::clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    print_vector(array, 10);
    std::cout << elapsed_secs;
}
