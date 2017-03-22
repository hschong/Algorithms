#include <iostream>

using namespace std;

#define RECURRSION

#ifdef RECURRSION
const int Len = 66;
const int Divs = 6;
void subdivide(char ar[], int low, int high, int level);
#else
struct structRegister
{
    int sn : 4;
    int : 4;
    bool goodIn : 1;
    bool goodTorgle : 1;
};
#endif

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
#ifdef RECURRSION
    int index;
    int max = Len - 2;
    int min = 0;
    char ruler[Len];

    ruler[Len - 1] = '\0';
    ruler[min] = ruler[max] = '|';

    for (index = 1; index < max; index++)   // initialize to blank ruler
        ruler[index] = ' ';
    cout << ruler << endl;

    for (index = 1; index <= Divs; index++)
    {
        subdivide(ruler, min, max, index);
        cout << ruler << endl;

        for (int i=1; i<max; i++)   // reset to blank ruler
            ruler[i] = ' ';
    }

#else
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
#endif
    
    return 0;
}

void subdivide(char ar[], int low, int high, int level)
{
    if (level == 0)
        return;

    int mid = (high + low) / 2;
    ar[mid] = '|';
    subdivide(ar, low, mid, level - 1);
    subdivide(ar, mid, high, level - 1);
}