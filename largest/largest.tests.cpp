#include "largest.hpp"
#include <gtest/gtest.h>

using namespace ::testing;



TEST(Largest, returns_95021_for_input_of_50_2_1_9)
{
    int numbers[] = { 50, 2, 1, 9};
    int size      = sizeof(numbers) / sizeof(int);

    ASSERT_EQ("95021", answer(numbers, size));
}

// given [5, 50, 56]    it returns "56550"    (56 + 5 + 50)

TEST(Largest, returns_56550_for_input_of_5_50_56) {
    int numbers[] = {5, 50, 56};
    int size      = sizeof(numbers) / sizeof(int);

    ASSERT_EQ("56550", answer(numbers, size) );

}

// given [420, 42, 423] it returns "42423420" (42 + 423 + 420)

TEST(Largest, returns_42423420_for_input_of_420_42_423)
{
    int numbers[] = { 420, 42, 423};
    int size      = sizeof(numbers) / sizeof(int);

    ASSERT_EQ("42423420", answer(numbers, size));
}


TEST(Largest, test_for_eight)
{
    int numbers[] = { 303, 11, 112, 21, 0, 2, 3, 44, 30};
    int size      = sizeof(numbers) / sizeof(int);

    ASSERT_EQ("44330330221112110", answer(numbers, size));
}