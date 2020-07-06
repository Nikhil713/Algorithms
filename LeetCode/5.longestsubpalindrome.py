# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: "cbbd"
# Output: "bb"


class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        newstr = ""
        if ( len (s) == 1):
            return s
        i=0
        while ( i < len(s) - 1 ):
            sub1 = helper(s,i,i)
            if ( len(sub1) > len (newstr)):
                newstr = sub1
            sub2 = helper(s,i,i+1)
            if ( len(sub2) > len (newstr)):
                newstr = sub2
            i+=1
        return newstr
            
            
            
def helper (s , left , right):
    while ( left >=0  and right < len(s) and s[left] == s[right]):
        left-=1
        right+=1
    return s[left + 1:right]