class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sortedDict = {}
        for i in strs:
            sortedstr = ''.join(sorted(i))
            if(sortedstr not in sortedDict):
                sortedDict[sortedstr] = []
            sortedDict[sortedstr].append(i)
        return list(sortedDict.values())