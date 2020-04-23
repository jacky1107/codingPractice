class Solution:
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    self.checkNeighbor(grid, i, j)
        return count

    def checkNeighbor(self, grid, i, j):
        if not (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0" ):
            grid[i][j] = "0"
            self.checkNeighbor(grid, i + 1, j)
            self.checkNeighbor(grid, i, j + 1)
            self.checkNeighbor(grid, i - 1, j)
            self.checkNeighbor(grid, i, j - 1)

grid = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,1,0,1]
]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = str(grid[i][j])

sol = Solution()
count = sol.numIslands(grid)
print(count)