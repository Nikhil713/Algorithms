# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] +nums[2]
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                tempsum = nums[i] + nums[left] +nums[right]
                if tempsum == target:
                    return target
                if abs(tempsum - target) < abs(res - target):
                    res = tempsum
                if tempsum < target:
                    left+=1
                if tempsum > target:
                    right-=1
                
        return res