#include <gtest/gtest.h>

extern "C"
{
#include "solution.h"

}

using namespace ::testing;

TEST(Strcat, test_for_equivalence) { 
  char s1[10] = "Hello"; 
  char s2[10] = " World!"; 
  char test1[100]; 
  strcpy(test1, s1); 
  strcat(test1, s2);
  strcat(test1, s1); 
    
  char test2[100]; 
  strcpy(test2, s1); 
  mystrcat(test2, s2, 0); 
  mystrcat(test2, s1, 0);

  EXPECT_STREQ(test1, test2);  
}

TEST(Strcat, test_for_small_size) { 
    EXPECT_NEAR(.02, get_time_for(100000, 100, STDCAT), .015); 
}

TEST(Strcat, test_for_normal_size) { 
    float expected_runtime = 0.15;  // in seconds
    float variance = expected_runtime * .50; 
    // flag is set to 0 to use customized strcat
    EXPECT_NEAR(expected_runtime, get_time_for(100000, 1000, 0), variance); 
}

TEST(Strcat, DISABLED_test_for_large_size) { 
//TEST(Strcat, test_for_large_size) {     
    float expected_runtime = 0.30;  // in seconds
    float variance = expected_runtime * .35; 
  
    // flag is set to 0 to use customized strcat
    EXPECT_NEAR(expected_runtime, get_time_for(100000, 2000, 0), variance);     
}
