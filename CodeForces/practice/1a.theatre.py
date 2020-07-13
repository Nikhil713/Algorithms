import math
n,m,a = map(int,input().split())
if n == 0 or m == 0:
    print(0)
else:
    height,width = 1,1
    width = max(width,math.ceil(n / a))

    height = max(height,math.ceil(m / a))

    print(width*height)