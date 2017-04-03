//
// Created by heese on 2017-04-04.
//

#ifndef RANDOMBINARYTREEFORBFS_CNODEFORRBT_H
#define RANDOMBINARYTREEFORBFS_CNODEFORRBT_H


class CNodeForRBT {
public:
    int m_Data;
    CNodeForRBT *m_pLeft, *m_pRight;

public:
    CNodeForRBT();
    CNodeForRBT(int data);
    CNodeForRBT(int data, CNodeForRBT *m_pLeft, CNodeForRBT *m_pRight);

    virtual ~CNodeForRBT();
};


#endif //RANDOMBINARYTREEFORBFS_CNODEFORRBT_H
