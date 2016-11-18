#include <iostream>
#include <vector>

#include "declaration.h"

void print_vector(std::vector<double> &array, int n) {
    for (int i = 0; i < n && i < array.size(); ++i)
        std::cout << array[i] << std::endl;
}

void print_vector(std::vector<date> &array, int n) {
    for (int i = 0; i < n && i < array.size(); ++i)
        std::cout << array[i].day << "/" << array[i].month << "/" << array[i].year << std::endl;
}

int compare_dates(date a, date b) {
    if (a.year < b.year) {
        return -1;
    } else {
        if (a.year == b.year) {
            if (a.month < b.month) {
                return -1;
            } else {
                if (a.month == b.month) {
                    if (a.day < a.day) {
                        return -1;
                    } else {
                        if (a.day == a.day) {
                            return 0;
                        } else {
                            return 1;
                        }
                    }
                } else {
                    return 1;
                }
            }
        } else {
            return 1;
        }
    }
}

void algorithm(std::vector<double> &array, int left, int right) {
    int i = left;
    int j = right;
    double pivot = array[(i + j) / 2];
    double temp;

    while (i <= j) {
        while (array[i] < pivot)
            i++;
        while (array[j] > pivot)
            j--;
        if (i <= j) {
            temp = array[i];
            array[i] = array[j];
            array[j] = temp;
            i++;
            j--;
        }
    }

    if (j > left) {
        algorithm(array, left, j);
    }

    if (i < right) {
        algorithm(array, i, right);
    }
}

void dates_algorithm(std::vector<date> &array, int left, int right) {
    int i = left;
    int j = right;
    date pivot = array[(i + j) / 2];
    date temp;

    while (i <= j) {
        while (compare_dates(array[i], pivot) == -1) {
             i++;
            }

        while (compare_dates(array[j], pivot) == 1) {
            j--;
        }

        if (i <= j) {
            temp = array[i];
            array[i] = array[j];
            array[j] = temp;
            i++;
            j--;
        }
    }

    if (j > left) {
        dates_algorithm(array, left, j);
    }

    if (i < right) {
        dates_algorithm(array, i, right);
    }
}

void quickSort(std::vector<double> &array) {
    print_vector(array, 10);
    std::cout << "===========================\n";
    algorithm(array, 0, array.size() - 1);
    print_vector(array, 10);
}

void quickSort(std::vector<date> &array) {
    std::cout << "===========================\n";
    print_vector(array, 10);
    std::cout << "===========================\n";
    dates_algorithm(array, 0, array.size() - 1);
    print_vector(array, 10);
}
