class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        productArray = [1] * len(nums)
        leftProduct = 1
        rightProduct = 1

        for i in range(len(nums)):
            productArray[i] = leftProduct
            leftProduct = leftProduct * nums[i]
        
        for i in range(len(nums) - 1, -1 ,-1):
            productArray[i] = productArray[i] * rightProduct
            rightProduct = rightProduct * nums[i]
        
        return productArray