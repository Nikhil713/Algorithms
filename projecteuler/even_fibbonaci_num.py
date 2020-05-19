#Project Euler Problem: 2

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i,k,s=1,2,0
    while(i<n or k<n):
        if(i%2==0 and i<n):
            s=s+i
        elif(k%2==0 and k<n):
            s=s+k
        i=i+k
        k=k+i
            
    print(s)        
