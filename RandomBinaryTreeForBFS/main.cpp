#include <iostream>
#include <cstdlib>
#include <ctime>
#include "CMyRandomBinaryTree.h"

using namespace std;

int main()
{
    CMyRandomBinaryTree myTree;
    unsigned int max_size = 0;
    unsigned int randNum = 0;

    srand((unsigned int)time(NULL));
    cout << "type your max size of tree : ";
    cin >> max_size;

    cout << endl << "make a random binary search tree!" << endl;
    for (int i=0; i<max_size; i++)
    {
        if (i%2 == 0)
            cout << endl;

        randNum = rand() % 100 + 1;
        if (NULL == myTree.search(randNum))
            myTree.insert(randNum);
        else
            --i;
    }

    cout << endl << endl << "print nodes at each depth." << endl;
    myTree.printNodesAtEachDepth();
    cout << endl << endl << "print nodes at second depth. the depth starts from zero." << endl;
    myTree.printNodesAtDepth(2);

    return 0;
}