#include "BSTree.hpp"

#include <iostream>
using namespace std;


// Need to also try out a non-recursive style
// That is, code an iterative version of the following function
//
void printNthNode(BSTNode* root, int N, int& index)
{
   cout << "Inside printNthNode...."
            << "N: " << N
            << " index: " << index << endl;

   if(root == 0)
       return;

   //For every Node go to the right of that node first.
   printNthNode(root->right, N, index);

   //Right has returned and now current node will be greatest
   if(index++ == N-1) {
     cout << "******" << N << "th node: " << root->value << endl;
     return;
   }

   //And at last go to the left
   printNthNode(root->left, N, index);
}

int BSTree:: KthLargest (BSTNode* h , int k ) {

    vector<int> v = inOrderTraversal(h);
    return v[k-1];

}

vector<int>& BSTree:: inOrderTraversal (BSTNode* h) {

    array.clear();

    if (h == 0 )
        return array;

    inOrderTraversalRec (h->right);
    array.push_back(h->value);
    inOrderTraversalRec (h->left);

    return array;
}

void BSTree:: inOrderTraversalRec (BSTNode* h) {

    if (h == 0)
        return;

    inOrderTraversalRec (h->right);
    array.push_back(h->value);
    inOrderTraversalRec (h->left);

}

BSTNode* BSTree:: secondLargestNode (BSTNode* h) {
    BSTNode* current = h;

    while (current) {

        // CASE 1: at the largest node
        // return the largest in the left node
        if (current->left && current->right == 0 )
            return maxNode(current->left);

        // CASE 2: current is the 2nd largest
        //   if current has no children on the left
        if (current->left == 0 &&
            // and current has one child on the right
            current->right && current->right->right == 0)
            return current;

        // CASE 3: continue searching...
        current = current->right;
    }

    return 0;
}

int BSTree:: secondLargest (BSTNode* h) {

    BSTNode* n = secondLargestNode(h);
    if (n)
        return n->value;
    return -1;
}

BSTNode* BSTree:: maxNode (BSTNode* h) {
    BSTNode *n = h;
    while (n->right)
        n = n->right;

    return n;

}

int BSTree:: max (BSTNode* h) {
    BSTNode* n = maxNode(h);
    return n ? n->value : -1;
}

BSTNode* BSTree:: minNode (BSTNode* h) {
    BSTNode *n = h;
    while (n->left)
        n = n->left;

    return n;
}

int BSTree:: min (BSTNode* h) {
    BSTNode* n = minNode(h);
    return n ? n->value : -1;
}

BSTNode* BSTree:: buildTree (int i1, int i2, int i3, int i4) {

    head = new BSTNode(i1);
    AddNode (i2);
    AddNode (i3);
    AddNode (i4);

    return head;
}

BSTNode* BSTree::AddNode (int val) {

    BSTNode* n = GetNode (head, val);
    if (val > n->value)
        n->right = new BSTNode (val);
    else
        n->left = new BSTNode (val);

    return n;

}


BSTNode* BSTree::GetNode (BSTNode* h, int val) {

    if (val > h->value) {
        if (h->right == 0)
            return h;
        return GetNode(h->right, val);
    }

    if (h->left == 0)
        return h;
    return GetNode(h->left, val);
}


