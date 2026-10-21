class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxVol = 0
        while (left < right):
            vol = min(height[left], height[right]) * (right - left)
            maxVol = max(vol, maxVol)
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
            
        return maxVol
            