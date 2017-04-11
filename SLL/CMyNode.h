//
// Created by Chong, HeeSeok on 2017. 4. 10..
//

#ifndef SLL_CMYNODE_H
#define SLL_CMYNODE_H

using namespace std;

template <typename T>
class CMyNode
{
protected:
    T data;
    CMyNode<T>* pNext;
    CMyNode<T>* pPrev;

public:
    CMyNode();
    virtual ~CMyNode();

    T getData() const;
    void setData(T data);

    CMyNode *getNext() const;
    void setNext(CMyNode *pNext);

    CMyNode *getPrev() const;
    void setPrev(CMyNode *pPrev);
};

template <typename T>
CMyNode<T>::CMyNode()
{
    pNext = NULL;
    pPrev = NULL;
}

template <typename T>
CMyNode<T>::~CMyNode()
{

}

template <typename T>
T CMyNode<T>::getData() const {
    return data;
}

template <typename T>
void CMyNode<T>::setData(T data) {
    CMyNode::data = data;
}

template <typename T>
CMyNode<T>* CMyNode<T>::getNext() const {
    return pNext;
}

template <typename T>
void CMyNode<T>::setNext(CMyNode *pNext) {
    CMyNode::pNext = pNext;
}

template <typename T>
CMyNode<T>* CMyNode<T>::getPrev() const {
    return pPrev;
}

template <typename T>
void CMyNode<T>::setPrev(CMyNode *pPrev) {
    CMyNode::pPrev = pPrev;
}

#endif //SLL_CMYNODE_H
