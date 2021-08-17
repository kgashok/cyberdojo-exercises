#include "index.h"
#include "unity.h"

void setUp(void)
{
}

void tearDown(void)
{
}

void test_match_at_start_of_string(void)
{
    char text[100] = "abcde";
    char pattern[30] = "abc";

    TEST_ASSERT_EQUAL(0, indexOf(text, pattern, FIRST));
}

void test_no_match_at_start_of_string(void)
{
    char text[100] = "abcde";
    char pattern[30] = "abz";

    TEST_ASSERT_EQUAL(-1, indexOf(text, pattern, FIRST));
}

void test_match_anywhere_in_string(void)
{
    char text[100] = "abcde";
    char pattern[30] = "cd";

    TEST_ASSERT_EQUAL(2, indexOf(text, pattern, FIRST));
}

void test_match_of_last_occurrence_in_string (void)
{
    char text[100] = "fox is always a fox.";
    char pattern[30] = "fox";

    TEST_ASSERT_EQUAL(16, indexOf(text, pattern, 0) ); 

}

void test_match_of_3rd_occurrence_in_string (void) 
{
    char text[100] = "indivisibility"; 
    char pattern[30] = "i";

    TEST_ASSERT_EQUAL(5, indexOf(text, pattern, 3) ); 

}

void test_match_case_insensitive_occurrence_in_string (void)
{
    char text[100] = "fox is a FOX.";
    char pattern[30] = "fox";

    TEST_ASSERT_EQUAL(9, indexOf(text, pattern, 0) ); 

}

void test_match_wraparound_in_string (void) { 
    char text [100] = "abcde"; 
    char pattern[30] = "dea"; 

    TEST_ASSERT_EQUAL(3, indexOf(text, pattern, FIRST) ); 

    TEST_ASSERT_EQUAL(3, indexOf("abcde", pattern, 0) ); 

}

void test_match_wraparound_in_string_with_duplicates (void) { 

    char text [100] = "abcdeade"; 
    char pattern[30] = "dea"; 

    TEST_ASSERT_EQUAL (6, indexOf(text, pattern, 0) ); 

}

