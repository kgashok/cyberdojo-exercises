#include "divisors.hpp"
#include <gtest/gtest.h>


#include <iostream>
using namespace std;


using namespace ::testing;

TEST(Divisor, DivisorCount)
{
    ASSERT_EQ(4, numOfDivisors(8));
}

TEST(Divisor, DivisorCountToBeEight )
{
    int n = 2 * 3 * 5;

    cout << "n: " << n << endl;

    ASSERT_EQ (8, numOfDivisors(n) ) ;
}

TEST(Divisor, ListOfNumbersHavingExactlyEightDivisors)
{

    EXPECT_EQ (2, countOfNumbersWithEightinRange(30) );
    EXPECT_EQ (180, countOfNumbersWithEightinRange(1000) );
    EXPECT_EQ (53, countOfNumbersWithEightinRange(340) );

}