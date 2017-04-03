//
// Created by heese on 2017-04-04.
//

#include "CMyRandomBinaryTree.h"
#include <iostream>

using namespace std;

CMyRandomBinaryTree::CMyRandomBinaryTree()
{
    m_pRoot = NULL;
}

CMyRandomBinaryTree::~CMyRandomBinaryTree() {

}

bool CMyRandomBinaryTree::isEmpty()
{
    if (m_pRoot == NULL)
        return true;
    else
        return false;
}

CNodeForRBT* CMyRandomBinaryTree::search(int data)
{
    return search(data, m_pRoot);
}

CNodeForRBT* CMyRandomBinaryTree::search(int data, CNodeForRBT *pNode)
{
    if (pNode == NULL)
    {
        cout << "can't find a node from the tree." << endl;
        return NULL;
    }

    if (data == pNode->m_Data)
    {
        return pNode;
    }
    else if (data < pNode->m_Data)
    {
        return search(data, pNode->m_pLeft);
    }
    else
    {
        return search(data, pNode->m_pRight);
    }

}

CNodeForRBT* CMyRandomBinaryTree::findMinNode(CNodeForRBT *pNode)
{
    if (pNode == NULL)
        return NULL;

    if (pNode->m_pLeft == NULL)
        return pNode;
    else
        return findMinNode(pNode->m_pLeft);
}

CNodeForRBT* CMyRandomBinaryTree::insert(int data)
{
    if (m_pRoot == NULL)
    {
        m_pRoot = new CNodeForRBT(data, NULL, NULL);
        return m_pRoot;
    }

    return insert(data, m_pRoot);
}

CNodeForRBT* CMyRandomBinaryTree::insert(int data, CNodeForRBT *pNode) // Tree should not be empty.
{
    if (pNode == NULL)
    {
        if (m_pRoot == NULL)
        {
            m_pRoot = new CNodeForRBT(data, NULL, NULL);
            return m_pRoot;
        }

        return new CNodeForRBT(data, NULL, NULL);
    }
    else if (data < pNode->m_Data)
    {
        pNode->m_pLeft = insert(data, pNode->m_pLeft);
    }
    else if (data > pNode->m_Data)
    {
        pNode->m_pRight = insert(data, pNode->m_pRight);
    }
    else
    {
        cout << "can't insert the node into the tree because the same value of the node was found from the tree." << endl;
        return NULL;
    }

    return pNode;
}

CNodeForRBT* CMyRandomBinaryTree::remove(int data, CNodeForRBT* pTargetNode, CNodeForRBT *pParentNode)
{
    if (pTargetNode == NULL)
    {
        cout << "can't remove a node in the tree." << endl;
        return NULL;
    }

    if (data < pTargetNode->m_Data)
    {
        return remove(data, pTargetNode->m_pLeft, pTargetNode);
    }
    else if( data > pTargetNode->m_Data)
    {
        return remove(data, pTargetNode->m_pRight, pTargetNode);
    }
    else    // Found the target node from the tree.
    {
        if (pTargetNode->m_pLeft == NULL && pTargetNode->m_pRight == NULL)  // No child
        {

            if (pTargetNode == pParentNode->m_pLeft)
            {
                pParentNode->m_pLeft = NULL;
            }
            else
            {
                pParentNode->m_pRight = NULL;
            }

            return pTargetNode;
        }
        else if (pTargetNode->m_pLeft != NULL && pTargetNode->m_pRight != NULL) // has 2 child nodes(left and right)
        {
            CNodeForRBT *pTemp = NULL;
            CNodeForRBT *pMinNode = findMinNode(pTargetNode->m_pRight);
            pTemp = remove(pMinNode->m_Data, pTargetNode, NULL);
            pTargetNode->m_Data = pMinNode->m_Data;

            return pTemp;
        }
        else    // An only child
        {
            CNodeForRBT *pChild = NULL;

            if (pTargetNode->m_pLeft != NULL)
            {
                pChild = pTargetNode->m_pLeft;
            }
            else
            {
                pChild = pTargetNode->m_pRight;
            }

            if (pParentNode->m_pLeft == pTargetNode)
            {
                pParentNode->m_pLeft = pChild;
            }
            else
            {
                pParentNode->m_pRight = pChild;
            }

            return pTargetNode;
        }
    }

}


