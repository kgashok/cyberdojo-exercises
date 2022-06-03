#include <gtest/gtest.h>

extern "C" {
#include "_utils.h"
#include "solution.h"

 
}
using namespace ::testing;



int main(int argc, char** argv) {
    
     /*Comment out the next 4 lines
     *if testing is not needed
     *
     ***********************************/
    ::testing::InitGoogleTest(&argc, argv);
    RUN_ALL_TESTS();
    puts("");
    puts("----------------------");
   
    return 0;
}
   



