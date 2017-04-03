#include <iostream>
#include "CMyStack.h"

int main() {
    CMyStack myStack;

    myStack.create(10);
    myStack.push("A");
    myStack.push("B");
    myStack.push("C");
    myStack.push("D");
    myStack.push("E");
    myStack.pop();
    myStack.push("A");
    myStack.push("A");
    myStack.push("B");
    myStack.push("C");
    myStack.push("D");
    myStack.push("E");
    myStack.push("F");
    myStack.printStack();

    myStack.pop();
    myStack.pop();
    myStack.pop();
    myStack.pop();
    myStack.pop();
    myStack.pop();
    myStack.pop();
    myStack.pop();
    myStack.pop();
    myStack.pop();
    myStack.pop();
    myStack.printStack();

    std::cout << std::endl << "Hello, World!";

    return 0;
}