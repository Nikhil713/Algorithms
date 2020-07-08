# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2 ):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                sum = nums[i] + nums [left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                        right -=1
                else:
                    temp = []
                    temp.append(nums[i])
                    temp.append(nums[left])
                    temp.append(nums[right])
                    res.append(temp)
                    while ( left < right and nums[left] == nums[left+1]   ):
                        left+=1
                    while (  left < right and nums[right] == nums[right-1]  ):
                        right-=1
                    left+=1
                    right-=1
                

        return(res)
                    
            