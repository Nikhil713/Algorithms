class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentLen = 0
        maxLen = 0
        currStr = ''
        pointer = 0
        while(pointer < len(s)):
            if s[pointer] in currStr:
                dupIndex = currStr.index(s[pointer])
                currStr = currStr[dupIndex + 1:]
            currStr += s[pointer]
            maxLen = max(maxLen, len(currStr))
            pointer += 1
        return maxLen