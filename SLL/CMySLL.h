//
// Created by heeseok.chong on 2017-04-02.
//

#ifndef SLL_CMYSLL_H
#define SLL_CMYSLL_H

#include <iostream>
#include <string>
#include "CMyNode.h"


using namespace std;

template <typename T>
class CMySLL
{
protected:
    CMyNode<T> *m_pHead;
    CMyNode<T> *m_pTail;

public:
    CMySLL();
    virtual ~CMySLL();

    bool isEmpty();
    bool printData(CMyNode<T> *pTargetNode);
    bool printAll();

    CMyNode<T>* search(const T data);
    CMyNode<T>* search(CMyNode<T> *pTargetNode);
    CMyNode<T>* findPrevNode(const CMyNode<T> *pTargetNode);

    CMyNode<T> *getHead() const;
    void setHead(CMyNode<T> *pNode);

    CMyNode<T> *getTail() const;
    void setTail(CMyNode<T> *pNode);

    CMyNode<T>* createNode(const T data);
    bool appendNode(const T data);
    bool insertNode(const T data, const unsigned int order);
    bool insertNode(const T data, const T targetData);

    bool removeNode();
    bool removeNode(CMyNode<T> *pTargetNode);
    bool removeNode(const T data);
};

template <typename T>
CMySLL<T>::CMySLL() {
    m_pHead = NULL;
    m_pTail = NULL;
}

template <typename T>
CMySLL<T>::~CMySLL() {

}

template <typename T>
CMyNode<T> *CMySLL<T>::getHead() const {
    return m_pHead;
}

template <typename T>
void CMySLL<T>::setHead(CMyNode<T> *pNode) {
    CMySLL<T>::m_pHead = pNode;
}

template <typename T>
CMyNode<T> *CMySLL<T>::getTail() const {
    return m_pTail;
}

template <typename T>
void CMySLL<T>::setTail(CMyNode<T> *pNode) {
    pNode->setNext(NULL);
    CMySLL<T>::m_pTail = pNode;
}

template <typename T>
bool CMySLL<T>::isEmpty() {
    if (CMySLL<T>::m_pHead == NULL)
        return true;
    else
        return false;
}

template <typename T>
CMyNode<T>* CMySLL<T>::createNode(const T data)
{
    CMyNode<T> *pNode = new CMyNode<T>;
    if (pNode == NULL)
        return NULL;

    if (isEmpty())
    {
        setHead(pNode);
        setTail(pNode);
    }

    pNode->setData(data);
    pNode->setNext(NULL);

    cout << "created a node = " << pNode->getData() << endl;
    return pNode;
}

template <typename T>
bool CMySLL<T>::appendNode(const T data)
{
    CMyNode<T> *pNode = createNode(data);
    if (pNode == NULL)
        return false;

    else
    {
        CMyNode<T> *pTail = getTail();
        pTail->pNext = pNode;
        setTail(pNode);
    }

    cout << "append a node = " << pNode->data << endl;
    return true;
}

template <typename T>
bool CMySLL<T>::insertNode(const T data, const unsigned int order)    // order's minimum is 1.
{
    CMyNode<T> *pNode = getHead();
    CMyNode<T> *pNewNode = NULL;

    if (pNode == NULL)
        return false;

    pNewNode = createNode(data);
    if (order > 1)
    {
        for (int i=1; i<order; i++)
        {
            pNode = pNode->getNext();
        }
    }

    pNewNode->setNext(pNode->getNext());
    pNode->setNext(pNewNode);

    if (pNode == getTail())
    {
        setTail(pNewNode);
    }

    cout << "insert a node after " << pNode->getData() << endl;
    return true;
}

template <typename T>
bool CMySLL<T>::insertNode(const T data, const T targetData)
{
    CMyNode<T> *pNewNode = createNode(data);
    CMyNode<T> *pNode = search(targetData);

    if (pNode == NULL || pNewNode == NULL)
        return false;

    pNewNode->setNext(pNode->getNext());
    pNode->setNext(pNewNode);

    if (pNode == getTail())
    {
        setTail(pNewNode);
    }

    cout << "insert a node after " << pNode->getData() << endl;
    return true;
}

template <typename T>
CMyNode<T>* CMySLL<T>::search(const T data)
{
    CMyNode<T> *pNode = getHead();
    if (pNode == NULL)
        return NULL;

    while (pNode->getData() != data)
    {
        pNode = pNode->getNext();
    }

    return pNode;
}

template <typename T>
CMyNode<T>* CMySLL<T>::search(CMyNode<T> *pTargetNode)
{
    CMyNode<T> *pNode = getHead();
    if (pNode == NULL || pTargetNode == NULL)
        return NULL;

    while (pNode != pTargetNode)
    {
        pNode = pNode->getNext();
    }

    return pNode;
}

template <typename T>
CMyNode<T>* CMySLL<T>::findPrevNode(const CMyNode<T> *pTargetNode) // pTargetNode should not be a pointer indicating head
{
    CMyNode<T> *pNode = getHead();
    if (pNode == NULL || pTargetNode == NULL)
        return NULL;

    while (pNode->getNext() != pTargetNode)
    {
        pNode = pNode->getNext();
    }

    return pNode;
}

template <typename T>
bool CMySLL<T>::removeNode()
{
    CMyNode<T> *pTail = getTail();
    if (pTail == NULL)
        return false;

    CMyNode<T> *pNode = findPrevNode(pTail);
    if (pNode != NULL)
    {
        setTail(pNode);
    }

    cout << "remove a node from tail = " << pTail->getData() << endl;
    delete pTail;

    return true;
}

template <typename T>
bool CMySLL<T>::removeNode(const T data)
{
    CMyNode<T> *pHead = getHead();
    CMyNode<T>* pNode = search(data);

    if (pNode == NULL)
        return false;

    cout << "remove a node(" << data << ") = " << pNode->getData() << endl;
    if (pNode == pHead)
    {
        setHead(pHead->getNext());
        delete pNode;
    }
    else if (pNode == getTail())
    {
        removeNode();
    }
    else
    {
        CMyNode<T> *pPrevNode = findPrevNode(pNode);
        pPrevNode->setNext(pNode->getNext());
        delete pNode;
    }

    return true;
}

template <typename T>
bool CMySLL<T>::removeNode(CMyNode<T> *pTargetNode)
{
    CMyNode<T> *pPrevNode = NULL;

    if (pTargetNode == NULL)
    {
        return false;
    }

    if (pTargetNode != getHead())
    {
        pPrevNode = findPrevNode(pTargetNode);
        pPrevNode->setNext(pTargetNode->getNext());
    }
    else
    {
        setHead(pTargetNode->getNext());
    }

    delete pTargetNode;

    return true;
}

template <typename T>
bool CMySLL<T>::printData(CMyNode<T> *pTargetNode)
{
    if (pTargetNode == NULL)
        return false;

    cout << pTargetNode->getData();

    return true;
}

template <typename T>
bool CMySLL<T>::printAll()
{
    CMyNode<T> *pNode = getHead();
    if (pNode == NULL)
        return false;

    while(pNode != NULL)
    {
        cout << pNode->getData() << " -> ";
        pNode = pNode->getNext();
    }
    cout << "NULL" << endl;

    return true;
}

#endif //SLL_CMYSLL_H
