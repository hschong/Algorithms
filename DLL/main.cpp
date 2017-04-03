#include <iostream>
#include "CMyDLL.h"

int main() {
    CMyDLL myDLL;

    myDLL.appendNode("A");
    myDLL.insertNode("B", 1);
    myDLL.insertNode("C", "A");
    myDLL.appendNode("D");
    myDLL.removeNode("C");
    myDLL.removeNode("A");
    myDLL.removeNode();

    myDLL.printAll();
    std::cout << "Head = ";
    myDLL.printData(myDLL.getHead());
    std::cout << ", Tail = ";
    myDLL.printData(myDLL.getTail());
    std::cout << std::endl << "Hello, World!";
    return 0;
}