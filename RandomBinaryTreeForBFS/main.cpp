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


    for (int i=0; i<max_size; i++)
    {
        randNum = rand() % 20 + 1;
        if (NULL == myTree.search(randNum))
            myTree.insert(randNum);
        else
            --i;
    }

    std::cout << "Hello, World!" << std::endl;
    return 0;
}