#include "BSTree.hpp"
#include <gtest/gtest.h>

using namespace ::testing;

TEST(BST, MaximumValueInBSTContaining2193Is9)
{
    BSTree b (2, 1, 9, 3);
    ASSERT_EQ(9, b.max(b.head) );
}

TEST(BST, MinimumValueInBSTContaining2193Is1)
{
    BSTree b (2, 1, 9, 3);
    ASSERT_EQ(1, b.min(b.head) );

    BSTree b2 (101, 102, 103, 105);
    ASSERT_EQ(101, b2.min(b2.head) );

}

TEST(BST, SecondLargestInBalancedBSTContaining5314789is8)
{
    BSTree b (5, 3, 1, 4, 7, 8, 9);
    ASSERT_EQ(8, b.secondLargest(b.head) );

    // finding 2nd largest in what must be an unbalanced BST
    BSTree b2 (104, 98, 80, 101, 200, 103, 1000);
    ASSERT_EQ(200, b2.secondLargest(b2.head) );

}

#include <iostream>
using namespace std;

void printNthNode(BSTNode* root, int N, int& count);

TEST(BST, KthLargestInBSTContaining5314789)
{

    BSTree b (5, 3, 1, 4, 7, 8, 9);

    EXPECT_EQ (8, b.KthLargest(b.head, 2) );
    EXPECT_EQ (3, b.KthLargest(b.head, 6) );


    int count = 0;
    for (int i : b.inOrderTraversal (b.head) ) {
        count++;
        cout << count << ". " << i << endl;
    }

}

TEST(BST, printingNthNodeInBSTContaining5314789)
{
    BSTree b (5, 3, 1, 4, 7, 8, 9);

    int count = 0;
    printNthNode(b.head, 2, count);
    cout << "next test...." << endl;
    count = 0;
    printNthNode(b.head, 6, count);
}


