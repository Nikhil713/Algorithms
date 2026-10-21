class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seenNumbers = {}
        for i in range(len(nums)):
            targetNum = target - nums[i]
            if(targetNum in seenNumbers):
                return [seenNumbers[targetNum], i]
            seenNumbers[nums[i]] = i