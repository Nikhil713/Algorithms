class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterOccurance = {}
        for char in s:
            letterOccurance[char] = letterOccurance.get(char,0) + 1
        for char in t:
            letterOccurance[char] = letterOccurance.get(char,0) - 1
        for i in letterOccurance:
            if letterOccurance[i] != 0:
                return False
        return True