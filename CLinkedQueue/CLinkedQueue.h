//
// Created by heese on 2017-04-03.
//

#ifndef RANDOMBINARYTREE_CLINKEDQUEUE_H
#define RANDOMBINARYTREE_CLINKEDQUEUE_H

#include "CMySLL.h"

class CLinkedQueue {
protected:
    Node    *m_pFront;
    Node    *m_pRear;
    CMySLL  *m_pList;
    unsigned int m_max_size;
    unsigned int m_size;

public:
    CLinkedQueue();
    virtual ~CLinkedQueue();

    void create(unsigned int max_size);
    void printQueue();

    bool enqueue(string data);
    bool dequeue();

    bool isFull();
    bool isEmpty();

    CMySLL *getM_pList() const;
    unsigned int getM_max_size() const;
    void setM_max_size(unsigned int m_max_size);

    unsigned int getM_size() const;
    void setM_size(unsigned int m_size);

    Node *getM_pFront() const;
    void setM_pFront(Node *pFront);

    Node *getM_pRear() const;
    void setM_pRear(Node *pRear);


};


#endif //RANDOMBINARYTREE_CLINKEDQUEUE_H
