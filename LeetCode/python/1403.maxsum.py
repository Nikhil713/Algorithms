class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        totsum = sum(nums)
        nums.sort(reverse = True)
        res = []
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            res.append(nums[i])
            if temp > totsum - temp:
                break
        return res
