#ifndef DECLARATION_H_INCLUDED
#define DECLARATION_H_INCLUDED

#include <vector>
#include <typeinfo>

struct date {
    int day;
    int month;
    int year;
};

struct algorithmPerformance {
    int cmp;
    int mov;
    int ovh;
    double time;
};

void generator(long, std::vector<double>&);
void generator(long, std::vector<date>&);

std::ostream& operator << (std::ostream &, date &);
int compare_dates(date, date);

template <typename T>
void print_vector(std::vector<T> &vector, unsigned n = 10) {
    for (typename std::vector<T>::size_type i = 0; i < n && i < vector.size(); ++i)
        std::cout << vector[i] << std::endl;
    std::cout << "===========================\n";
}

template <typename T>
int cmp(T x, T y) {
    return (x>y) ? 1 : ((x<y) ? -1 : 0);
}

template <typename T>
void swap(std::vector<T>& vector, int i, int j) {
    if(i == j)
        return;

    T temp;
    temp = vector[i];
    vector[i] = vector[j];
    vector[j] = temp;
}

template <typename T>
void showSortTitle(std::string algorithmName, std::vector<T>& vector) {
    std::cout << algorithmName << " " << typeid(T).name() << " SIZE: " << vector.size() << std::endl;
    print_vector(vector, 10);
}

#endif // DECLARATION_H_INCLUDED
