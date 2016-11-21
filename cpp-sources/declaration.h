#ifndef DECLARATION_H_INCLUDED
#define DECLARATION_H_INCLUDED

#include <vector>

struct date {
    int day;
    int month;
    int year;
};

struct operations {
    int cmp;
    int mov;
    int ovh;
}

void generator(long, std::vector<double>&);
void generator(long, std::vector<date>&);

std::ostream& operator << (std::ostream &, date &);
int compare_dates(date, date);

template <typename T>
void print_vector(std::vector<T> &array, unsigned n) {
    for (unsigned i = 0; i < n && i < array.size(); ++i)
        std::cout << array[i] << std::endl;
}

template <typename T>
int cmp(T x, T y) {
    return (x>y) ? 1 : ((x<y) ? -1 : 0);
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

#endif // DECLARATION_H_INCLUDED
