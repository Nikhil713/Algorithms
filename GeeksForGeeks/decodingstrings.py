A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

You are an FBI agent. You have to determine the total number of ways that message can be decoded.
Note: An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and If there are leading 0’s, extra trailing 0’s and two or more consecutive 0’s then it is an invalid string.

Example :
Given encoded message "123",  it could be decoded as "ABC" (1 2 3) or "LC" (12 3) or "AW"(1 23).
So total ways are 3.

Input:
First line contains the test cases T.  1<=T<=1000
Each test case have two lines
First is length of string N.  1<=N<=40
Second line is string S of digits from '0' to '9' of N length.

Example:
Input:
2
3
123
4
2563
Output:
3
2
 
 #code

def helper(data,k,mem):
    
    
    s = len(data) - k
    
    if k == 0:
        return(1)
    
    if data[s] == 0:
        return(0)
        
    if (mem[k] != None):
        return(mem[k])
        
    result = helper(data,k-1,mem)
    
    
    if (k >= 2 and int(data[s:s+2]) <=26 ):
        result += helper(data,k-2,mem)
    
    mem[k] = result
    print (result ,k)
    return result
    

def num_ways(data,k):
    mem = [None]*(k+1)
    count = helper(data,k,mem)
    return count
    
    
    
tcase = int(input())

for i in range(tcase):
    
    size = int(input())
    data = input()
    
    count = 0
    count = num_ways(data,len(data))
    
    for j in range(data.count('0')):
        n= data.index('0')
        if int(data[n-1]) >= 3:
            count = 0
            break
        data = data[n+1:]
        # print(data)
    print(count)
        
        