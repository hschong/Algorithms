//
// Created by heeseok.chong on 2017-04-04.
//

#ifndef RANDOMBINARYTREEFORBFS_CNODEFORRBT_H
#define RANDOMBINARYTREEFORBFS_CNODEFORRBT_H


class CNodeForRBT {
public:
    unsigned int m_Data;
    unsigned int m_Depth;
    CNodeForRBT *m_pLeft, *m_pRight;

public:
    CNodeForRBT();
    CNodeForRBT(int data);
    CNodeForRBT(int data, CNodeForRBT *m_pLeft, CNodeForRBT *m_pRight);

    virtual ~CNodeForRBT();

    unsigned int getM_Depth() const;
    void setM_Depth(unsigned int depth);
};


#endif //RANDOMBINARYTREEFORBFS_CNODEFORRBT_H
