#include <iostream>
#ifdef _WIN32
#include <cstdlib>
#endif

void inc_1(int c, int d) // Call by Value
{
    c++; d++;
    printf("inc_1 : a - %d b - %d\n", c, d);
}

void inc_2(int *e, int *f) // Call by Pointer
{
    (*e)++; (*f)++;
    printf("inc_2 : a - %d b - %d\n", *e, *f);
}

void inc_3(int &g, int &h) // Call by Reference
{
    g++; h++;
    printf("inc_3 : a - %d b - %d\n", g, h);
    printf("inc_3 : g - %f h - %f\n", &g, &h);
}


int main() 
{
    std::cout << "Hello, World!" << std::endl;
    int a = 5, b = 10;

    inc_1(a, b);
    printf("main : a - %d b - %d\n", a, b);
    inc_2(&a, &b);
    printf("main : a - %d b - %d\n", a, b);
    inc_3(a, b);
    printf("main : a - %f b - %f\n", &a, &b);
    printf("main : a - %d b - %d\n", a, b);

#ifdef _WIN32
    system("pause");
#endif
    return 0;
}