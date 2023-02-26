from math import sqrt

k = 0
for x in range(5,500,4):
    n = 0
    comp = set()
    for i in range(1,int(sqrt(x))):
        p = sqrt(x - i*i)
        if float(p).is_integer():
            comp.add(i)
            comp.add(int(p))
    l = len(comp)
    
    if l > 2 and l < 5:
        max1 = max(comp)
        comp.remove(max1)
        max2 = max(comp)
        comp.remove(max2)
        min1 = min(comp)
        comp.remove(min1)
        min2 = min(comp)
        comp.remove(min2)
        print(f'{x} = {min1}^2 + {max1}^2 = {min2}^2 + {max2}^2')
        k+=1
        if k==10: break
