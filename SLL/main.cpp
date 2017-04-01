#include <iostream>
#include "CMySLL.h"

int main() {
    CMySLL mySLL;

    mySLL.appendNode("A");
    mySLL.insertNode("B", 1);
    mySLL.insertNode("C", "A");
    mySLL.printAll();
    std::cout << "Head = ";
    mySLL.printData(mySLL.getHead());
    std::cout << ", Tail = ";
    mySLL.printData(mySLL.getTail());
    std::cout << std::endl << "Hello, World!" << std::endl;
    return 0;
}