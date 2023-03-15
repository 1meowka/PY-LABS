for i in range (1,1001):
    g = len(str(i))
    if i == (i ** 2) % 10 ** g:
        print(i)
