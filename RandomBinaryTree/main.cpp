#include <iostream>
#include "CMyLinkedQueue.h"

using namespace std;



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