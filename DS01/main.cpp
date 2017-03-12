#include <iostream>

using namespace std;

void inc_1(int c, int d) // Call by Value
{
    c++; d++;
    cout << "inc_1 : a = " << c << ", b = " << d << "\n";
}

void inc_2(int *e, int *f) // Call by Pointer
{
    (*e)++; (*f)++;
    cout << "inc_2 : a = " << *e << ", b = " << *f << "\n";
}

void inc_3(int &g, int &h) // Call by Reference
{
    g++; h++;
    cout << "inc_3 : &g = " << &g << ", &h = " << &h << "\n";
    cout << "inc_3 : a = " << g << ", b = " << h << "\n";
}


int main() 
{
    std::cout << "Hello, World!" << std::endl;
    int a = 5, b = 10;

    inc_1(a, b);
    cout << "main after inc_1 : a = " << a << ", b = " << b << "\n";
    inc_2(&a, &b);
    cout << "main after inc_2 : a = " << a << ", b = " << b << "\n";

    cout << "main : &a = " << &a << ", &b = " << &b << "\n";
    inc_3(a, b);
    cout << "main after inc_3  : a = " << a << ", b = " << b << "\n";
    cin.get();
    return 0;
}