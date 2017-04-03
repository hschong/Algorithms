//
// Created by heese on 2017-04-03.
//

#include "CLinkedQueue.h"
#include <iostream>

using namespace std;

CLinkedQueue::CLinkedQueue()
{
    CLinkedQueue::m_pList = NULL;
    CLinkedQueue::m_pFront = NULL;
    CLinkedQueue::m_pRear = NULL;
    CLinkedQueue::m_max_size = 0;
    CLinkedQueue::m_size = 0;
}

CLinkedQueue::~CLinkedQueue() {
    delete m_pList;
}

void CLinkedQueue::create(unsigned int max_size)
{
    CLinkedQueue::m_pList = new CMySLL;
    setM_max_size(max_size);
    setM_size(0);
}

void CLinkedQueue::printQueue()
{
    getM_pList()->printAll();
}

bool CLinkedQueue::isFull()
{
    if (getM_size() == getM_max_size())
        return true;
    else
        return false;
}

bool CLinkedQueue::isEmpty()
{
    if (getM_size() == 0)
        return true;
    else
        return false;
}

bool CLinkedQueue::enqueue(string data)
{
    if (isFull())
    {
        cout << "Queue is full!" << endl;
        return false;
    }

    CMySLL *pList = getM_pList();
    if (pList == NULL)
    {
        cout << "There is no queue!" << endl;
        return false;
    }

    if (!pList->appendNode(data))
    {
        cout << "can't enqueue!" << endl;
        return false;
    }

    if (getM_pFront() == NULL)  // enqueue node into the queue as  the front if the queue is empty.
    {
        setM_pFront(pList->getHead());
        setM_pRear(pList->getTail());
    }

    cout << "enqueue " << getM_pRear()->data << " into the queue!" << endl;
    setM_size(getM_size()+1);
    setM_pRear(pList->getTail());

    return true;
}

bool CLinkedQueue::dequeue()
{
    if (isEmpty())
    {
        cout << "Queue is empty!" << endl;
        return false;
    }

    CMySLL *pList = getM_pList();
    if (pList == NULL)
    {
        cout << "There is no queue!" << endl;
        return false;
    }

    cout << "dequeue " << getM_pFront()->data << " from the queue!" << endl;
    if (!pList->removeNode(getM_pFront()))
    {
        cout << "can't enqueue!" << endl;
        return false;
    }

    setM_size(getM_size()-1);
    setM_pFront(pList->getHead());

    return true;
}

CMySLL *CLinkedQueue::getM_pList() const {
    return m_pList;
}

Node *CLinkedQueue::getM_pFront() const {
    return m_pFront;
}

void CLinkedQueue::setM_pFront(Node *pFront) {
    CLinkedQueue::m_pFront = pFront;
}

Node *CLinkedQueue::getM_pRear() const {
    return m_pRear;
}

void CLinkedQueue::setM_pRear(Node *pRear) {
    CLinkedQueue::m_pRear = pRear;
}

unsigned int CLinkedQueue::getM_max_size() const {
    return m_max_size;
}

void CLinkedQueue::setM_max_size(unsigned int max_size) {
    CLinkedQueue::m_max_size = max_size;
}

unsigned int CLinkedQueue::getM_size() const {
    return m_size;
}

void CLinkedQueue::setM_size(unsigned int size) {
    CLinkedQueue::m_size = size;
}



