# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

# Example 2:

# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]

 

# Constraints:

#     m == mat.length
#     n == mat[i].length
#     1 <= n, m <= 50
#     1 <= matrix[i][j] <= 10^5.
#     All elements in the matrix are distinct.

nbismoi's avatar
nbismoi
97

March 29, 2020 6:46 AM

930 VIEWS

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minrow = {min(r) for r in matrix}
        maxcol = {max(c) for c in zip(*matrix)} # it is like iterating through column values
        return list(minrow & maxcol)

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row,col = [],[]
        for i in matrix:
            row.append(min(i))
        for i in range(len(matrix[0])):
            temp = matrix[0][i]
            for j in range(len(matrix)):
                temp = max(temp,matrix[j][i])
            col.append(temp)
        res = []
        for i in row:
            if i in col:
                res.append(i)
        return res
