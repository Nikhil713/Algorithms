class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for i in A:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(A)//2):
            A[2*i] = even[i]
            A[2*i+1] = odd[i]
        return A