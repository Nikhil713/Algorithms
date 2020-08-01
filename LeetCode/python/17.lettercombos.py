# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if not digits:
            return []
        ret = []
        def helper(ret,cur,index):
            if (index == len(digits)):
                ret.append(''.join(cur[:]))
                return
            for c in d[digits[index]]:
                cur.append(c)
                helper(ret,cur,index+1)
                cur.pop()
        helper(ret,[],0)
        return ret