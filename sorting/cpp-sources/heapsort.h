#ifndef HEAPSORT_H_INCLUDED
#define HEAPSORT_H_INCLUDED

#include "declaration.h"

algorithmPerformance heapsort(std::vector<double>);
algorithmPerformance heapsort(std::vector<date>);

template <typename T>
void sift(std::vector<T>& vector,
          typename std::vector<T>::size_type heapSize,
          typename std::vector<T>::size_type siftNode,
          int cmpFn(T, T),
          algorithmPerformance &perfomance) {

    typename std::vector<T>::size_type i, j;
    j = siftNode;
    perfomance.ovh++; // j initialize

    do {
        i = j;
        perfomance.ovh++; // update i

        perfomance.ovh++; // test condition
        if((2*i + 1) < heapSize) {
            perfomance.cmp++; // compare elements
            if (cmpFn(vector[j], vector[2*i + 1]) == -1) {
                j = 2*i + 1;
                perfomance.ovh++; // update j
            }
        }

        perfomance.ovh++; // test condition
        if((2*i + 2) < heapSize) {
            perfomance.cmp++; // compare elements
            if (cmpFn(vector[j], vector[2*i + 2]) == -1) {
                j = 2*i + 2;
                perfomance.ovh++; // update j
            }
        }

        swap(vector, i, j);
        perfomance.mov += 3; // swap element

        perfomance.ovh++; // check while condition
    } while(i != j);
}

template <typename T>
void makeInitialHeap(std::vector<T> &vector,
                    int cmpFn(T, T),
                    algorithmPerformance &perfomance) {
    perfomance.ovh++; // i initialize

    for(int i = vector.size() - 1; i >= 0; --i) {
        perfomance.ovh += 2; // i decrement, test complete cycle
        sift(vector, vector.size(), i, cmpFn, perfomance);
    }
}

template <typename T>
void heapsort_algorithm(std::vector<T> &vector,
                        int cmpFn(T, T),
                        algorithmPerformance &perfomance) {
    makeInitialHeap(vector, cmpFn, perfomance);

    perfomance.ovh++; // i initialize
    for(typename std::vector<T>::size_type i = vector.size() - 1; i > 0; --i) {
        perfomance.ovh += 2; // i decrement, test complete cycle

        swap(vector, i, 0);
        perfomance.mov += 3; // swap element

        sift(vector, i, 0, cmpFn, perfomance);
    }
}

#endif // HEAPSORT_H_INCLUDED
