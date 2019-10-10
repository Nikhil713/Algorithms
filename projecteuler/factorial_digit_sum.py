T=int(input().strip())
for a in range(1,T+1):
    N=int(input().strip())
    p=1
    s=0
    for i in range(2,N+1):
        p=p*i
    
    while(p!=0):
        a=p%10
        p=p//10
        s=s+a
    print(s)    
