class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        noOfIslands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            grid[r][c] = '0'
            if r + 1 < rows and grid[r+1][c] == '1':
                dfs(r+1, c)
            if r - 1 >= 0 and grid[r-1][c] == '1':
                dfs(r-1, c)
            if c + 1 < cols and grid[r][c+1] == '1':
                dfs(r, c+1)
            if c - 1 >= 0 and grid[r][c-1] == '1':
                dfs(r, c-1)
                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    noOfIslands += 1
                    print(noOfIslands)
                    dfs(i,j)

        return noOfIslands