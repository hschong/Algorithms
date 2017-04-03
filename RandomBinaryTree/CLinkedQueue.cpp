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

bool CLinkedQueue::enqueue(string data)
{
    int max_size = getM_max_size();
    int size = getM_size();

    if (size == max_size)
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

    size++;
    setM_size(size);
    setM_pFront(pList->getHead());
    setM_pRear(pList->getTail());

    return true;
}

bool CLinkedQueue::dequeue()
{
    int size = getM_size();

    if (size == 0)
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

    if (!pList->removeNode(getM_pFront()))
    {
        cout << "can't enqueue!" << endl;
        return false;
    }

    size--;
    setM_size(size);
    setM_pFront(pList->getHead());
    setM_pRear(pList->getTail());

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



