#include <iostream>
#include <cstdlib>
#include <fstream>
using namespace std;

void realsGenerator() {
    ofstream realsFile;
    realsFile.open ("../data/reals");

    srand((unsigned)time(NULL));

    for (int i = 0; i < 10000; i++ ){
        double r = ((double)rand() / (double)(RAND_MAX));
        realsFile << r << endl;
    }

    realsFile.close();
}
