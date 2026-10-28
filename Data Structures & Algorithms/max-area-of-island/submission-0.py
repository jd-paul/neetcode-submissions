class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        max_area = 0
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                if self.grid[i][j] == 1:
                    area = self.recurse(i, j)

                    max_area = max(area, max_area)
        
        return max_area
    
    # Look up, down, left, and right
    def recurse(self, i, j):
        if i < 0 or i >= len(self.grid): # Out of range checks
            return 0
        if j < 0 or j >= len(self.grid[i]):
            return 0
        
        if self.grid[i][j] == 1:
            self.grid[i][j] = 0
            return 1 + self.recurse(i+1, j) + self.recurse(i-1, j) + self.recurse(i, j+1) + self.recurse(i, j-1)
        
        return 0