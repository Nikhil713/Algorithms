class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if( abs(arr[i] - arr[j]) <= a):
                        if( abs( arr[j] - arr[k]) <= b):
                            if( abs(arr[i] - arr[k]) <= c):
                                res += 1
        return res