# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example:

# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = permutations(nums)
        return set(nums)