class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = temp = nums[0]
        for i in nums[1:]:
            temp = max(i,temp + i)
            res = max(res,temp)
        return res