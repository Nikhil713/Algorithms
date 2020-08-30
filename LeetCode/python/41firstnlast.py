class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            return [nums.index(target),len(nums) - 1 - nums[::-1].index(target)]
        return [-1,-1]