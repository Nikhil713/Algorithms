class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            sortedWord = ''.join(sorted(i))
            if sortedWord not in hashmap:
                hashmap[sortedWord] = [i]
            else:
                hashmap[sortedWord].append(i)
        arr = []
        for i in hashmap.items():
            arr.append(i[1])
        return arr