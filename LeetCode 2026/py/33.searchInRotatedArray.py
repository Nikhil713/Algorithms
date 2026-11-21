class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            # Left side sorted
            if nums[left] <= nums[mid]:
                # Target in left sorted part
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right side sorted
            else:
                # Target in right sorted part
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1