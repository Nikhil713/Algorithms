# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321

# Example 2:

# Input: -123
# Output: -321

# Example 3:

# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



class Solution:
    def reverse(self, x: int) -> int:
        arr = [num for num in str(x)]
        size = len(arr)-1
        flag=0
        while(arr[size] == 0):
            size-=1
        if(arr[0]=='-'):
            newarr= arr[1:size+1]
            flag = 1
        else:
            newarr= arr[:size+1]
        newarr = newarr[::-1]
        num=int("".join(map(str,newarr)))
        if flag == 1:
            num*=-1
        if(abs(num) > 2**31 -1):
            return 0
        return num