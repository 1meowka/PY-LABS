from math import *

# n = int(input())
n = 10

f = lambda x: exp(sin(x)) - x
g = lambda x: log(1 + sqrt(x)) - cos(x)

A = [[f(i) + g(j) for j in range (1, n + 1)] for i in range(1, n + 1)]
print(sqrt(max(abs(A[i][i]) for i in range(n))))



