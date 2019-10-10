import math
T=int(input().strip())
for i in range(1,T+1):
  t=int(input().strip())
  k=(-1+math.sqrt(1+8*t))
  if(k%2==0):
    print(int(k/2))
  else:
    print(-1)
   
