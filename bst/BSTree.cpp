#include "BSTree.hpp"
#include <gtest/gtest.h>
using namespace ::testing;

TEST(BST, LargestElementInBSTContaining2193Is9)
{
    BSTree b (2, 1, 9, 3);
    ASSERT_EQ(9, b.max() );
}