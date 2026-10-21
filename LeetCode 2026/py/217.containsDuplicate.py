class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seenNumbers = set()
        for i in nums:
            if i in seenNumbers:
                return True
            seenNumbers.add(i)
        return False