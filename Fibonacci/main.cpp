#include <iostream>

struct Matrix_2x2
{
    unsigned long arrayData[2][2];
};

Matrix_2x2 matrix;

Matrix_2x2 matrix_2x2_multiply(Matrix_2x2 matrix_a, Matrix_2x2 matrix_b)
{
    matrix.arrayData[0][0] = matrix_a.arrayData[0][0] * matrix_b.arrayData[0][0] +
                             matrix_a.arrayData[0][1] * matrix_b.arrayData[1][0];

    matrix.arrayData[0][1] = matrix_a.arrayData[0][0] * matrix_b.arrayData[0][1] +
                             matrix_a.arrayData[1][0] * matrix_b.arrayData[1][1];

    matrix.arrayData[1][0] = matrix_a.arrayData[1][0] * matrix_b.arrayData[0][0] +
                             matrix_a.arrayData[1][1] * matrix_b.arrayData[1][0];

    matrix.arrayData[1][1] = matrix_a.arrayData[1][0] * matrix_b.arrayData[0][1] +
                             matrix_a.arrayData[1][1] * matrix_b.arrayData[1][1];

    return matrix;
}

Matrix_2x2 matrix_2x2_power(Matrix_2x2 matrix, int n)
{
    if (n>1)
    {
        matrix = matrix_2x2_power(matrix, n/2);
        matrix = matrix_2x2_multiply(matrix, matrix);

        if (n&1)
        {
            Matrix_2x2 base;
            base.arrayData[0][0] = 1;
            base.arrayData[0][1] = 1;
            base.arrayData[1][0] = 1;
            base.arrayData[1][1] = 0;

            matrix = matrix_2x2_multiply(matrix, base);
        }
    }

    return matrix;
}

unsigned long getFibonacci(unsigned long n)
{
    Matrix_2x2 matrix4Fibonacci;
    matrix4Fibonacci.arrayData[0][0] = 1;
    matrix4Fibonacci.arrayData[0][1] = 1;
    matrix4Fibonacci.arrayData[1][0] = 1;
    matrix4Fibonacci.arrayData[1][1] = 0;
    matrix4Fibonacci = matrix_2x2_power(matrix4Fibonacci, n);

    return matrix4Fibonacci.arrayData[0][1];
}

unsigned long solution(unsigned long n)
{
    if (0 == n)
        return 0;
    else if (1 == n || 2 == n)
        return 1;

    return getFibonacci(n);
}

int main() {
    unsigned long n;
    std::cout << "Type your n =  ";
    std::cin >> n;

    std::cout << "f(" << n <<") = " << solution(n) << std::endl;

    return 0;
}