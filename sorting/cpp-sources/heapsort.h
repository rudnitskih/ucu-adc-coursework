#ifndef HEAPSORT_H_INCLUDED
#define HEAPSORT_H_INCLUDED

#include "declaration.h"

algorithmPerformance heapsort(std::vector<double>);
algorithmPerformance heapsort(std::vector<date>);

template <typename T>
void sift(std::vector<T>& vector,
          typename std::vector<T>::size_type heapSize,
          typename std::vector<T>::size_type siftNode,
          int cmp(T, T)) {

    typename std::vector<T>::size_type i, j;
    j = siftNode;

    do {
        i = j;
        if(((2*i + 1) < heapSize) && cmp(vector[j], vector[2*i + 1]) == -1)
            j = 2*i + 1;
        if(((2*i + 2) < heapSize) && cmp(vector[j], vector[2*i + 2]) == -1)
            j = 2*i + 2;

        swap(vector, i, j);
    } while(i != j);
}

template <typename T>
void makeInitialHeap(std::vector<T> &vector, int cmp(T, T)) {
    for(int i = vector.size() - 1; i >= 0; --i) {
        sift(vector, vector.size(), i, cmp);
    }
}

template <typename T>
void heapsort_algorithm(std::vector<T> &vector, int cmp(T, T)) {
    makeInitialHeap(vector, cmp);

    for(typename std::vector<T>::size_type i = vector.size() - 1; i > 0; --i) {
        swap(vector, i, 0);
        sift(vector, i, 0, cmp);
    }
}

#endif // HEAPSORT_H_INCLUDED
