class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numCount = {}
        for i in nums:
            numCount[i] = numCount.get(i,0) + 1
        sortedNumCount = {k: v for k, v in sorted(numCount.items(), key=lambda item: item[1], reverse = True)}
        result = []
        for i in sortedNumCount:
            result.append(i)
            if(len(result) == k):
                break
        return result