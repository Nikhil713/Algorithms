# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # xbin = str(bin(x)).replace("0b","")
        # ybin = str(bin(y)).replace("0b","")
        # count = 0
        # xlen = len(xbin)
        # ylen = len(ybin)
        # maxlen = max(xlen,ylen)
        # if xlen > ylen:
        #     ybin = '0' * (xlen - ylen) + ybin
        # if ylen > xlen:
        #     xbin = '0' * (ylen - xlen) + xbin
        # for i in range(len(xbin)):
        #     if xbin[i] != ybin[i]:
        #         count+=1
        # return count
        
        x = x^y
        res = str(bin(x)).replace("0b","")
        return (res.count('1'))