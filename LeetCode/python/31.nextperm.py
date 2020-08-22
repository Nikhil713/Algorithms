class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 2
        while(index >= 0):
            if nums[index] < nums[index+1]:
                break
            index-=1
        
        if index < 0:
            nums.sort()
            return nums
        
        nindex = index + 1
        while nindex < len(nums) and nums[nindex] > nums[index]:
            nindex += 1
        nums[nindex-1],nums[index] = nums[index], nums[nindex-1]
        nums[index+1:] = nums[index+1:][::-1]