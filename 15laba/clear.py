from math import *

n = 10

def f(x):
    return exp(sin(x)) - x

def g(x):
    return log(1 + sqrt(x)) - cos(x)

A = []
for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        row.append(f(i) + g(j))
    A.append(row)

max_val = 0.0
for i in range(n):
    abs_val = abs(A[i][i])
    if abs_val > max_val:
        max_val = abs_val

result = sqrt(max_val)

print(result)
