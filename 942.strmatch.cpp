class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        arr = []
        low = 0
        high = len(S)
        i = 0
        while ( i < len(S)):
            if S[i] == 'I':
                arr.append(low)
                low += 1
            if S[i] == 'D':
                arr.append(high)
                high -= 1
            i += 1
        if S[-1] == 'D':
            arr.append(high)
        else:
            arr.append(low)
        return arr