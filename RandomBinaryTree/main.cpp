#include <iostream>

using namespace std;

struct Node
{
    int     data;
    Node    *pLeft;
    Node    *pRight;
};

class CMySLL
{
protected:
    Node    *m_pRoot;
    int     m_depthOfTree;

public:
    CMySLL()
    {
        m_pRoot = NULL;
        m_depthOfTree = 0;
    }

    virtual ~CMySLL()
    {
        destroyTree(m_pRoot);
    }

    int getDpethOfTree(int maxNodes)
    {
        if (maxNodes == 0 || maxNodes == 1)
            return 0;

        return 1 + getDpethOfTree(maxNodes/2);
    }

    Node* getRoot()
    {
        return m_pRoot;
    }

    int getDepthOfTree(Node* pNode)
    {
        if (pNode == NULL)
            return 0;

        return 1+ getDepthOfTree(pNode->pLeft) + getDepthOfTree(pNode->pRight);
    }

    Node* addNode(Node *pRoot, Node *pNewNode)
    {
        if (pRoot == NULL)
        {
            pRoot = pNewNode;
            return pRoot;
        }

        if (pRoot->pLeft == NULL)
        {
            pRoot->pLeft = pNewNode;
            return pRoot;
        }
        else
        {
            if (pRoot->pRight == NULL)
            {
                pRoot->pRight = pNewNode;
                return pRoot->pLeft;
            }
            else
            {
                return addNode(pRoot->pLeft, pNewNode);
            }
        }

    }

    Node* destroyTree(Node *pRoot)
    {
        if (pRoot == NULL)
            return NULL;

        Node *pLeft = pRoot->pLeft;
        Node *pRight = pRight->pRight;

        if (NULL == destroyTree(pLeft))
        {
            if (pRight != NULL)
            {
                delete pRight;
                return NULL;
            }

            delete pRoot;
            return NULL;
        }

        destroyTree(pRight);
        destroyTree(pRoot);

        return NULL;
    }

    Node* createNode(int randomNum)
    {
        Node *pNode = new Node;
        pNode->data = randomNum;
        pNode->pLeft = NULL;
        pNode->pRight = NULL;

        return pNode;
    }
};

int main() {
    int max = -1;
    int randomNum = -1;
    int depth = -1;
    Node *pNode = NULL;
    Node *pRoot = NULL;

    std::cout << "Type your maximum nodes to make a random binary tree : " << endl;
    std::cin >> max;

    CMySLL mySLL;
    pRoot = mySLL.getRoot();
    depth = mySLL.getDpethOfTree(max);

    for (int i=0; i<max; i++)
    {
        pNode = mySLL.createNode(randomNum);
        pRoot = mySLL.addNode(pRoot, pNode);
    }

    std::cout << "Hello, World!" << std::endl;
    return 0;
}