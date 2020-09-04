class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums1 = nums[:]
        nums += nums
        res = []
        for i in range(len(nums1)):
            temp = -1
            for j in range(i,len(nums)):
                if nums[j] > nums1[i]:
                    temp = nums[j]
                    break
            res.append(temp)
        return res