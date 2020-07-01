# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

# Return 0 if the array contains less than 2 elements.

# Example 1:

# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
#              (3,6) or (6,9) has the maximum difference 3.

# Example 2:

# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        maxdiff=0
        i=0
        while(i< len(nums) - 1):
            diff = nums[i+1] - nums[i]
            if diff > maxdiff:
                maxdiff = diff
            i+=1
        return maxdiff
            