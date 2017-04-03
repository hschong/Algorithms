//
// Created by heese on 2017-04-03.
//

#include "CMyStack.h"
#include "CMySLL.h"
#include <iostream>

using namespace std;

CMyStack::CMyStack()
{
    m_pSLL = NULL;
    m_size = -1;
    m_max_size = -1;
}

CMyStack::~CMyStack()
{
    delete m_pSLL;
}

void CMyStack::create(unsigned int size)
{
    m_pSLL = new CMySLL;
    setM_max_size(size);
    setM_size(0);
}

bool CMyStack::destroy()
{

}

bool CMyStack::isFull()
{
    unsigned int max_size = getM_max_size();
    unsigned int size = getM_size();

    if (max_size == size)
        return true;
    else
        return false;
}

bool CMyStack::isEmpty()
{
    unsigned int size = getM_size();

    if (size == 0)
        return true;
    else
        return false;
}

bool CMyStack::push(string data)
{
    CMySLL *pSLL = getM_pSLL();
    unsigned int size = getM_size();

    if (isFull())
    {
        cout << "Can't push the data into the stack because the stack is full." << endl;
        return false;
    }

    pSLL->appendNode(data);
    size++;
    setM_size(size);

    return true;
}

bool CMyStack::pop()
{
    CMySLL *pSLL = getM_pSLL();
    unsigned int size = getM_size();

    if (isEmpty())
    {
        cout << "Can't pop from the stack because the stack is empty." << endl;
        return false;
    }

    pSLL->removeNode();
    size--;
    setM_size(size);

    return true;
}

void CMyStack::printStack()
{
    CMySLL *pSLL = getM_pSLL();
    unsigned int size = getM_size();

    if (size == 0)
        std::cout << "Stack is empty" << std::endl;
    else
    {
        pSLL->printAll();
    }
}

int CMyStack::getM_size() const {
    return m_size;
}

void CMyStack::setM_size(int size) {
    CMyStack::m_size = size;
}

int CMyStack::getM_max_size() const {
    return m_max_size;
}

void CMyStack::setM_max_size(int m_max_size) {
    CMyStack::m_max_size = m_max_size;
}

CMySLL *CMyStack::getM_pSLL() const {
    return m_pSLL;
}
