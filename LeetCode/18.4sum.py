# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if not nums or len(nums)<4:
            return []
        nums.sort()
        i=0
        while ( i <len(nums) -3) :
            j = i+1
            while ( j <len(nums) - 2 ):
                left = j + 1
                right = len(nums) - 1
                while (left < right) : 
                    sum1 = nums[i] + nums[j] + nums[right] + nums[left]
                    if sum1 == target :
                        temp = []
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[left])
                        temp.append(nums[right])
                        res.append(temp)
                        left+=1
                        right-=1
                        
                    else:
                        if sum1 < target :
                            left+=1
                        else:
                            right-=1
                j+=1
            i+=1
        res1 = []
        for i in range(len(res)):
            if res[i] not in res1:
                res1.append(res[i])
        return res1