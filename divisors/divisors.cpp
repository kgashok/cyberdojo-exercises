#include "divisors.hpp"

int numOfDivisors(int n)
{

    int count = 0;
    for (int i = n/2 ; i > 1; i--)
        if (n % i == 0) count++;


    return count+2;
}


int isNumOfDivisorsEight (int n) { return numOfDivisors(n) == 8; }

#include <iostream>
using namespace std;

int countOfNumbersWithEightinRange (int range) {

    int count = 0;
    for (int i = 1; i <= range; i++ )
        if (isNumOfDivisorsEight (i) ) {
            cout << i << " ";
            count++;
    }

    cout << "Total number of numbers with exactly 8 divisors: " \
         << count << endl;

    return count;
}