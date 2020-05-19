#program to find thne largest sum of digits of power
N=int(input())
S=0
big_sum=0
for a in range(2,N+1):
    for b in range(1,N+1):
        S=0
        num=a**b
        while(num!=0):
            d=num%10
            num=num//10
            S=S+d
        if(big_sum<S):   
            big_sum=S
print(big_sum)
