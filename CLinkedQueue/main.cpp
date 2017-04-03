#include <iostream>
#include "CLinkedQueue.h"

using namespace std;

int main() {
    CLinkedQueue myQueue;

    myQueue.create(10);
    myQueue.enqueue("A");
    myQueue.enqueue("B");
    myQueue.enqueue("C");
    myQueue.enqueue("D");
    myQueue.enqueue("E");
    myQueue.enqueue("F");
    myQueue.enqueue("G");
    myQueue.enqueue("H");
    myQueue.enqueue("I");
    myQueue.enqueue("J");
    myQueue.enqueue("K");
    myQueue.enqueue("L");
    myQueue.printQueue();

    myQueue.dequeue();
    myQueue.dequeue();
    myQueue.dequeue();
    myQueue.dequeue();
    myQueue.dequeue();
    myQueue.printQueue();
    myQueue.dequeue();
    myQueue.dequeue();
    myQueue.dequeue();
    myQueue.dequeue();
    myQueue.dequeue();
    myQueue.dequeue();
    myQueue.printQueue();

    std::cout << "Hello, World!" << std::endl;
    return 0;
}