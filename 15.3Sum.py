class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2 ):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1 
            while(left < right):
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                
                    while (left < right) and (nums[left] == nums[left - 1]):
                        left += 1
                    while (left < right) and  (nums[right] == nums[right + 1]):
                        right -= 1
                        
                if(currentSum < 0):
                    left += 1
                if(currentSum > 0):
                    right -= 1
        return result