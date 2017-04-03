//
// Created by heese on 2017-04-03.
//
#include "CMySLL.h"

#ifndef STACK_CMYSTACK_H
#define STACK_CMYSTACK_H


class CMyStack {
protected:
    CMySLL  *m_pSLL;
    int     m_size;
    int     m_max_size;

public:
    CMyStack();
    virtual ~CMyStack();

    void create(const unsigned int size);
    bool destroy();

    bool isFull();
    bool isEmpty();
    bool push(string data);
    bool pop();
    void printStack();

    int getM_max_size() const;
    void setM_max_size(int m_max_size);
    int getM_size() const;
    void setM_size(int size);
    CMySLL *getM_pSLL() const;

};


#endif //STACK_CMYSTACK_H
