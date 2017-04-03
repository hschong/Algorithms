//
// Created by heeseok.chong on 2017-04-02.
//

#include "CMySLL.h"
#include <iostream>

using namespace std;

CMySLL::CMySLL() {
    m_pHead = NULL;
    m_pTail = NULL;
}

CMySLL::~CMySLL() {

}

Node *CMySLL::getHead() const {
    return m_pHead;
}

void CMySLL::setHead(Node *pNode) {
    CMySLL::m_pHead = pNode;
}

Node *CMySLL::getTail() const {
    return m_pTail;
}

void CMySLL::setTail(Node *pNode) {
    pNode->pNext = NULL;
    CMySLL::m_pTail = pNode;
}

bool CMySLL::isEmpty() {
    if (CMySLL::m_pHead == NULL)
        return true;
    else
        return false;
}

Node* CMySLL::createNode(const string data)
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

    cout << "created a node = " << pNode->data << endl;
    return pNode;
}

bool CMySLL::appendNode(const string data)
{
    Node *pNode = createNode(data);
    if (pNode == NULL)
        return false;

    else
    {
        Node *pTail = getTail();
        pTail->pNext = pNode;
        setTail(pNode);
    }

    cout << "append a node = " << pNode->data << endl;
    return true;
}

bool CMySLL::insertNode(const string data, const unsigned int order)    // order's minimum is 1.
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

    if (pNode == getTail())
    {
        setTail(pNewNode);
    }

    cout << "insert a node after " << pNode->data << endl;
    return true;
}

bool CMySLL::insertNode(const string data, const string targetData)
{
    Node *pNewNode = createNode(data);
    Node *pNode = search(targetData);

    if (pNode == NULL || pNewNode == NULL)
        return false;

    pNewNode->pNext = pNode->pNext;
    pNode->pNext = pNewNode;

    if (pNode == getTail())
    {
        setTail(pNewNode);
    }

    cout << "insert a node after " << pNode->data << endl;
    return true;
}

Node* CMySLL::search(const string data)
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

Node* CMySLL::findPrevNode(const Node *pTargetNode) // pTargetNode should not be a pointer indicating head
{
    if (pTargetNode == NULL)
        return NULL;

    Node *pNode = getHead();
    if (pNode == pTargetNode)
        return NULL;

    while (pNode->pNext != pTargetNode)
    {
        pNode = pNode->pNext;
    }

    return pNode;
}

bool CMySLL::removeNode()
{
    Node *pTail = getTail();
    if (pTail == NULL)
        return false;

    Node *pNode = findPrevNode(pTail);
    if (pNode != NULL)
    {
        setTail(pNode);
    }

    cout << "remove a node from tail = " << pTail->data << endl;
    delete pTail;

    return true;
}

bool CMySLL::removeNode(const string data)
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
        Node *pPrevNode = findPrevNode(pNode);
        pPrevNode->pNext = pNode->pNext;
        delete pNode;
    }

    return true;
}

bool CMySLL::printData(Node *pNode)
{
    if (pNode == NULL)
        return false;

    cout << pNode->data;

    return true;
}

bool CMySLL::printAll()
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
