if __name__ == '__main__':
    arr=[]
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        arr.append([name,score])
    arr.sort(key = lambda x: x[1])
    narr=[]
    for i in range(1,n):
        narr.append(arr[i][0])
        if(arr[i][1]!=arr[i+1][1]):
            break
narr.sort()
for i in range(len(narr)):
    print(narr[i])
