# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input:

# "bbbab"

# Output:

# 4

# One possible longest palindromic subsequence is "bbbb".

 

# Example 2:
# Input:

# "cbbd"

# Output:

# 2

# One possible longest palindromic subsequence is "bb".

 

# Constraints:

#     1 <= s.length <= 1000
#     s consists only of lowercase English letters.


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def recursion(i,j):
            if i == j:
                return 1
            elif i > j:
                return 0
            if s[i] == s[j]:
                return 2 + recursion(i+1,j-1)
            else:
                return max(recursion(i+1,j),recursion(i,j-1))
        return recursion(0,len(s)-1)