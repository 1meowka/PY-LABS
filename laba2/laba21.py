for i in range(1, 1001): #Способ 2
    res = len(str(i))
    if i == (i**2) % 10 ** res: 
        print(i)
