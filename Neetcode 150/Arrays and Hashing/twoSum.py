class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in indices:
                return([indices[complement], i])
            indices[n] = i
        return []


# Brute Force Approach

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in nums[i+1:]:
#                 j = nums.index(complement,i+1)
#                 return([i, j])
