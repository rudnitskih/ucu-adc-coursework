#include <iostream>
#include <vector>

void printArray(std::vector<double> &array, int n)
{
    for (int i = 0; i < n; ++i)
        std::cout << array[i] << std::endl;
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

void quickSort(std::vector<double> &array) {
    int n = sizeof(array)/sizeof(array[0]);
    printArray(array, 10);
    std::cout << "===========================";
    algorithm(array, 0, array.size());
    printArray(array, 10);
}
