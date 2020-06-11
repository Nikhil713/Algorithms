#code

tcase = int(input())

for i in range(tcase):
    
    arr = list(input())
    
    stack = []
    maxdiff = 0
    size = len(arr)
    j=0
    
    print (arr)
    for i in range(size):
        
        if (arr[i] == '('):
            stack.push('(')
            j+=1
        if (arr[i] == ')') and stack.empty() != 0:
            stack.pop()
            j+=1
        if (len(stack) == 0):
            maxdiff = j
            j=0
        print (stack , j ,maxdiff)
        
    print(maxdiff)