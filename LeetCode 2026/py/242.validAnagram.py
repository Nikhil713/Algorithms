class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmaps = {}
        hashmapt = {}
        for i in s:
            hashmaps[i]  = hashmaps.get(i, 0) + 1
        for i in t:
            hashmapt[i]  = hashmapt.get(i, 0) + 1
        if hashmaps == hashmapt:
            return True
        return False
        # if(len(s) != len(t)):
        #     return False
        # if(sorted(s) == sorted(t)):
        #     return True
        # return False