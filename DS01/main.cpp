#include <iostream>

using namespace std;

struct structRegister
{
    int sn : 4;
    int : 4;
    bool goodIn : 1;
    bool goodTorgle : 1;
};

void inc_1(int c, int d) // Call by Value
{
    c++; d++;
    cout << "inc_1 : a = " << c << ", b = " << d << endl;
}

void inc_2(int *e, int *f) // Call by Pointer
{
    (*e)++; (*f)++;
    cout << "inc_2 : a = " << *e << ", b = " << *f << endl;
}

void inc_3(int &g, int &h) // Call by Reference
{
    g++; h++;
    cout << "inc_3 : &g = " << &g << ", &h = " << &h << endl;
    cout << "inc_3 : a = " << g << ", b = " << h << endl;
}

int main() 
{
    structRegister regA;
    int a = 5, b = 10;

    std::cout << "Hello, World!" << std::endl;
    inc_1(a, b);
    cout << "main after inc_1 : a = " << a << ", b = " << b << endl;
    inc_2(&a, &b);
    cout << "main after inc_2 : a = " << a << ", b = " << b << endl;

    cout << "main : &a = " << &a << ", &b = " << &b << endl;
    inc_3(a, b);
    cout << "main after inc_3  : a = " << a << ", b = " << b << endl;
    cout << sizeof(regA) << ", " << sizeof(int) << endl;

    cin.get();
    return 0;
}