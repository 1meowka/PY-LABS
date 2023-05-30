from math import exp, sin, sqrt, log, cos

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

max_abs = 0
for i in range(n):
    if abs(A[i][i]) > max_abs:
        max_abs = abs(A[i][i])

result = sqrt(max_abs)
print(result)
