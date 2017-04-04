//
// Created by heese on 2017-04-04.
//

#ifndef RANDOMBINARYTREEFORBFS_CMYRANDOMBINARYTREE_H
#define RANDOMBINARYTREEFORBFS_CMYRANDOMBINARYTREE_H

#include <unwind.h>
#include "CNodeForRBT.h"

class CMyRandomBinaryTree {
protected:
    CNodeForRBT *m_pRoot;
public:
    CNodeForRBT *getM_pRoot() const;

public:
    CMyRandomBinaryTree();
    virtual ~CMyRandomBinaryTree();

    bool isEmpty();
    CNodeForRBT* search(int data);
    CNodeForRBT* search(int data, CNodeForRBT *pNode);
    CNodeForRBT* findMinNode(CNodeForRBT *pNode);
    CNodeForRBT* insert(int data);
    CNodeForRBT* insert(int data, CNodeForRBT *pNode);
    CNodeForRBT* remove(int data, CNodeForRBT* pTargetNode, CNodeForRBT *pParentNode);
    void printNodesAtEachDepth();
    void printNodesAtDepth(unsigned int depth);

};


#endif //RANDOMBINARYTREEFORBFS_CMYRANDOMBINARYTREE_H
