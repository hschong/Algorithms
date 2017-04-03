//
// Created by heese on 2017-04-03.
//

#include "CMyDLL.h"
#include <iostream>

CMyDLL::CMyDLL() {
    m_pHead = NULL;
    m_pTail = NULL;
}

CMyDLL::~CMyDLL() {

}

Node *CMyDLL::getHead() const {
    return m_pHead;
}

void CMyDLL::setHead(Node *pNode) {
    CMyDLL::m_pHead = pNode;
}

Node *CMyDLL::getTail() const {
    return m_pTail;
}

void CMyDLL::setTail(Node *pNode) {
    pNode->pNext = NULL;
    CMyDLL::m_pTail = pNode;
}

bool CMyDLL::isEmpty() {
    if (CMyDLL::m_pHead == NULL)
        return true;
    else
        return false;
}

Node* CMyDLL::createNode(const string data)
{
    Node *pNode = new Node;
    if (pNode == NULL)
        return NULL;

    if (isEmpty())
    {
        setHead(pNode);
        setTail(pNode);
    }

    pNode->data = data;
    pNode->pNext = NULL;
    pNode->pPrev = NULL;

    cout << "created a node = " << pNode->data << endl;
    return pNode;
}

bool CMyDLL::appendNode(const string data)  // add a node after tail.
{
    Node *pNode = createNode(data);
    if (pNode == NULL)
        return false;

    else
    {
        Node *pTail = getTail();
        pTail->pNext = pNode;
        pNode->pPrev = pTail;
        setTail(pNode);
    }

    cout << "append a node = " << pNode->data << endl;
    return true;
}

bool CMyDLL::insertNode(const string data, const unsigned int order)    // order's minimum is 1.
{
    Node *pNode = getHead();
    Node *pNewNode = NULL;

    if (pNode == NULL)
        return false;

    pNewNode = createNode(data);
    if (order > 1)
    {
        for (int i=1; i<order; i++)
        {
            pNode = pNode->pNext;
        }
    }

    pNewNode->pNext = pNode->pNext;
    pNode->pNext = pNewNode;
    pNewNode->pPrev = pNode;
    pNode->pNext->pPrev = pNewNode;

    if (pNode == getTail())
    {
        setTail(pNewNode);
    }

    cout << "insert a node after " << pNode->data << endl;
    return true;
}

bool CMyDLL::insertNode(const string data, const string targetData)
{
    Node *pNewNode = createNode(data);
    Node *pNode = search(targetData);

    if (pNode == NULL || pNewNode == NULL)
        return false;

    pNewNode->pNext = pNode->pNext;
    pNode->pNext = pNewNode;
    pNewNode->pPrev = pNode;
    pNewNode->pNext->pPrev = pNewNode;

    if (pNode == getTail())
    {
        setTail(pNewNode);
    }

    cout << "insert a node after " << pNode->data << endl;
    return true;
}

Node* CMyDLL::search(const string data)
{
    Node *pNode = getHead();
    if (pNode == NULL)
        return NULL;

    while (pNode->data != data)
    {
        pNode = pNode->pNext;
    }

    return pNode;
}

bool CMyDLL::removeNode()
{
    Node *pTail = getTail();
    if (pTail == NULL)
        return false;

    Node *pNode = pTail->pPrev;
    setTail(pNode);

    cout << "remove a node from tail = " << pTail->data << endl;
    delete pTail;

    return true;
}

bool CMyDLL::removeNode(const string data)
{
    Node *pHead = getHead();
    Node* pNode = search(data);

    if (pNode == NULL)
        return false;

    cout << "remove a node(" << data << ") = " << pNode->data << endl;
    if (pNode == pHead)
    {
        setHead(pHead->pNext);
        delete pNode;
    }
    else if (pNode == getTail())
    {
        removeNode();
    }
    else
    {
        Node *pPrevNode = pNode->pPrev;
        pPrevNode->pNext = pNode->pNext;
        pNode->pNext->pPrev = pPrevNode;
        delete pNode;
    }

    return true;
}

bool CMyDLL::printData(const Node *pNode)
{
    if (pNode == NULL)
        return false;

    cout << pNode->data;

    return true;
}

bool CMyDLL::printAll()
{
    Node *pNode = getHead();
    if (pNode == NULL)
        return false;

    while(pNode != NULL)
    {
        cout << pNode->data << " -> ";
        pNode = pNode->pNext;
    }
    cout << "NULL" << endl;

    return true;
}