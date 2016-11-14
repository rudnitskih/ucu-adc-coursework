#ifndef DECLARATION_H_INCLUDED
#define DECLARATION_H_INCLUDED

#include <vector>

struct date {
    int day;
    int month;
    int year;
};

void sortData();
void quickSort(std::vector<double>&);
void quickSort(std::vector<date>&);

void generator(long, std::vector<double>&);
void generator(long, std::vector<date>&);
#endif // DECLARATION_H_INCLUDED
