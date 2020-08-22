class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i,v in enumerate(nums):
            if v in hashmap and i - hashmap[v] <= k:
                return True
            hashmap[v] = i
        return False