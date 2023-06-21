import math
p=3
sinA=1/2
n=6
for i in range(1,14):
    sinA=math.sqrt((1-math.sqrt(1-sinA*sinA))/2)
    n=2*n
    p = n * sinA
    print(p)