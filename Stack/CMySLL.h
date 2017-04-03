//
// Created by heeseok.chong on 2017-04-02.
//

#ifndef SLL_CMYSLL_H
#define SLL_CMYSLL_H

#include <string>

using namespace std;

typedef struct tagNode
{
    string data;
    struct tagNode *pNext;
} Node;

class CMySLL
{
protected:
    Node *m_pHead;
    Node *m_pTail;

public:
    CMySLL();
    virtual ~CMySLL();

    bool isEmpty();
    bool printData(Node *pTargetNode);
    bool printAll();

    Node* search(const string data);
    Node* search(Node *pTargetNode);
    Node* findPrevNode(const Node *pTargetNode);

    Node *getHead() const;
    void setHead(Node *pNode);

    Node *getTail() const;
    void setTail(Node *pNode);

    Node* createNode(const string data);
    bool appendNode(const string data);
    bool insertNode(const string data, const unsigned int order);
    bool insertNode(const string data, const string targetData);

    bool removeNode();
    bool removeNode(Node *pTargetNode);
    bool removeNode(const string data);
};


#endif //SLL_CMYSLL_H
