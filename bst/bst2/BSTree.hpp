#ifndef BST_INCLUDED
#define BST_INCLUDED

class BSTNode {
public:
    int value;
    BSTNode* left;
    BSTNode* right;
public:
    BSTNode (int v) {
        value = v;
        left  = 0;
        right = 0;
    }

};

#include <vector>

class BSTree {
public:
    BSTNode* head;
    std::vector<int> array;

    BSTree (int i1, int i2, int i3, int i4) {
        buildTree(i1, i2, i3, i4);
    }
    BSTree (int i1, int i2, int i3, int i4, int i5, int i6, int i7) {
        buildTree (i1, i2, i3, i4);
        AddNode(i5), AddNode(i6), AddNode(i7);
    }

    int      max(BSTNode*);
    int      min(BSTNode*);
    BSTNode* maxNode(BSTNode*);
    BSTNode* minNode(BSTNode*);

    int      secondLargest(BSTNode*);
    BSTNode* secondLargestNode(BSTNode*);

    int      KthLargest(BSTNode*, int);
    BSTNode* KthLargestNode(BSTNode*, int);

    std::vector<int>& inOrderTraversal (BSTNode*);
    void              inOrderTraversalRec (BSTNode*);


private:
    BSTNode* buildTree (int, int, int, int);
    BSTNode* AddNode (int);
    BSTNode* GetNode (BSTNode*, int);

};

#endif