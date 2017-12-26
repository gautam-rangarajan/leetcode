class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    self.sinkIsland(grid, i, j)
                    count += 1
        
        return count
        
    def sinkIsland(self, grid, i, j):
        if i < 0 or j < 0:
            return
        if i > len(grid)-1 or j > len(grid[0])-1:
            return
        if grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        
        self.sinkIsland(grid, i-1, j)
        self.sinkIsland(grid, i+1, j)
        self.sinkIsland(grid, i, j-1)
        self.sinkIsland(grid, i, j+1)
        
        return