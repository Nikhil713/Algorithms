# https://leetcode.com/problems/valid-palindrome/

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:

# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1=''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                s1+=s[i]
        if s1 == s1[::-1]:
            return True
        else:
            return False
        