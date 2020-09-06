class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            res.append('Push')
            if i not in target:
                res.append('Pop')
            if i == target[-1]:
                break
        return res