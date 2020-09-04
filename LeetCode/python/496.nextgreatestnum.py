class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            temp = -1
            start = nums2.index(i)
            for j in nums2[start:]:
                if i < j:
                    temp = j
                    break
            res.append(temp)
        return res