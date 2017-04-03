//
// Created by heese on 2017-04-03.
//

#ifndef DLL_CMYDLL_H
#define DLL_CMYDLL_H

#include <string>

using namespace std;

typedef struct tagNode
{
    string data;
    struct tagNode *pPrev;
    struct tagNode *pNext;
} Node;


class CMyDLL {
    Node *m_pHead;
    Node *m_pTail;

public:
    CMyDLL();
    virtual ~CMyDLL();

    bool isEmpty();
    bool printData(const Node *pNode);
    bool printAll();

    Node* search(const string data);

    Node *getHead() const;
    void setHead(Node *pNode);

    Node *getTail() const;
    void setTail(Node *pNode);

    Node* createNode(const string data);
    bool appendNode(const string data);
    bool insertNode(const string data, const unsigned int order);
    bool insertNode(const string data, const string targetData);

    bool removeNode();
    bool removeNode(const string data);
};


#endif //DLL_CMYDLL_H
