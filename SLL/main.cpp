#include <iostream>
#include "CMySLL.h"

int main() {
    CMySLL<string> mySLL;

    mySLL.createNode("A");
    mySLL.insertNode("B", 1);
    mySLL.insertNode("C", "A");
    mySLL.printAll();
    std::cout << "Head = ";
    mySLL.printData(mySLL.getHead());
    std::cout << ", Tail = ";
    mySLL.printData(mySLL.getTail());

    /*CMySLL<int> mySLL;

    mySLL.createNode(1);
    mySLL.insertNode(2, 1);
    mySLL.insertNode(3, 1);
    mySLL.printAll();
    std::cout << "Head = ";
    mySLL.printData(mySLL.getHead());
    std::cout << ", Tail = ";
    mySLL.printData(mySLL.getTail());*/

    std::cout << std::endl << "Hello, World!" << std::endl;

    return 0;
}