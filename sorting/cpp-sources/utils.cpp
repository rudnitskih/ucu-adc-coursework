#include <iostream>
#include <fstream>
#include "declaration.h"

std::ostream& operator << (std::ostream &o, date &a) {
  o << a.day << "/" << a.month << "/" << a.year;
  return o;
}

int compare_dates(date a, date b) {
    if (cmp(a.year, b.year) != 0)
        return cmp(a.year, b.year);

    if (cmp(a.month, b.month) != 0)
        return cmp(a.month, b.month);

    return cmp(a.day, b.day);
}

void saveToFile(algorithmPerformance resultsOfPerfomance, std::string name, std::string typeOfData) {
    std::ofstream fileWithResults;

    fileWithResults.open("../program_results/" + name + "_" + typeOfData + ".csv", std::ofstream::out | std::ofstream::app);
    fileWithResults
        << resultsOfPerfomance.records
        << "; "
        << resultsOfPerfomance.time
        << "; "
        << resultsOfPerfomance.cmp
        << "; "
        << resultsOfPerfomance.mov
        << "; "
        << resultsOfPerfomance.ovh
        << "\n";
    fileWithResults.close();
}
