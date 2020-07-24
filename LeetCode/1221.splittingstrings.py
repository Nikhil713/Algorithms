# Balanced strings are those who have equal quantity of 'L' and 'R' characters.

# Given a balanced string s split it in the maximum amount of balanced strings.

# Return the maximum amount of splitted balanced strings.

 

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:

# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

# Example 3:

# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".

# Example 4:

# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

 

# Constraints:

#     1 <= s.length <= 1000
#     s[i] = 'L' or 'R'

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lcount = 0
        rcount = 0
        i = 0
        tcount = 0
        while ( i < len(s)):
            if s[i] == 'R':
                rcount += 1
            if s[i] == 'L':
                lcount +=1
            if lcount == rcount:
                tcount+=1
                rcount = 0
                lcount = 0
            i+=1
        return tcount