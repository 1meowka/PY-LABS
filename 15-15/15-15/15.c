//gcc 15.c -fPIC -shared -o 15.so -lm -Ofast -march=native

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double f(int x)
{
    return exp(sin(x)) - x;
}

double g(int x)
{
    return log(1 + sqrt(x)) - cos(x);
}
double func(int n)
{
    //scanf("%i", &n);
    n += 1;
    double A[n][n];
    for (int i = 1; i < n; i++)
    {
        for (int j = 1; j < n; j++)
        {
            A[i][j] = f(i) + g(j);
        }
    }
    double max = abs(A[0][0]);
    for (int i = 1; i < n; i++)
    {
        if(abs(A[i][i]) > max)
            max = fabs(A[i][i]);
    }
    return sqrt(max);
}
int main()
{
    printf("%f", func(10));
}