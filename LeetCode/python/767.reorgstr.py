# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

# Example 1:

# Input: S = "aab"
# Output: "aba"

# Example 2:

# Input: S = "aaab"
# Output: ""

# Note:

#     S will consist of lowercase letters and have length in range [1, 500].

class Solution:
    def reorganizeString(self, S: str) -> str:
        a = sorted(sorted(S),key = S.count)
        l = len(a)//2
        a[1::2],a[::2] = a[:l],a[l:]
        return ''.join(a) * (a[-1:] != a[-2:-1])