class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while(left < right):
            sumNumbers = numbers[left] + numbers[right]
            if sumNumbers < target:
                left += 1
            elif sumNumbers > target:
                right -= 1
            elif sumNumbers == target:
                break
        return [left + 1,right + 1]