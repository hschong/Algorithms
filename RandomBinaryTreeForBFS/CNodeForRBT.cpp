//
// Created by heese on 2017-04-04.
//

#include "CNodeForRBT.h"
#include <cstdlib>

CNodeForRBT::CNodeForRBT()
{
    this->m_pLeft = this;
    this->m_pRight = this;
    this->m_Data = 0;
}

CNodeForRBT::CNodeForRBT(int data)
{
    CNodeForRBT(data, NULL, NULL);
}

CNodeForRBT::CNodeForRBT(int data, CNodeForRBT *pLeft, CNodeForRBT *pRight) : m_Data(data), m_pLeft(pLeft), m_pRight(pRight)
{
    m_pLeft = pLeft;
    m_pRight = pRight;
    m_Data = data;
}

CNodeForRBT::~CNodeForRBT() {

}
