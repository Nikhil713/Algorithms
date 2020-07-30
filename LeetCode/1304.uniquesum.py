# Given an integer n, return any array containing n unique integers such that they add up to 0.

 

# Example 1:

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

# Example 2:

# Input: n = 3
# Output: [-1,0,1]

# Example 3:

# Input: n = 1
# Output: [0]

 

# Constraints:

#     1 <= n <= 1000

class Solution:
    def sumZero(self, n: int) -> List[int]:
        # arr = []
        # j = 0
        # for i in range(n//2):
        #     j+=1
        #     arr.append(j)
        #     arr.append(-1*j)
        # if n%2 != 0:
        #     arr.append(0)
        # return arr
        return(range(1-n,n,2))