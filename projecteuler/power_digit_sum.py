T=int(input())
for i in range(T):
    N=int(input())
    power=2**N
    S=0
    while(power!=0):
        d=power%10
        power=power//10
        S=S+d
    print(S)    
