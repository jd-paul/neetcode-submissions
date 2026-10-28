"""
Once we visit an island, we flip it to a zero.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.counter = 0
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                if self.grid[i][j] == "1":
                    self.recurse(i, j)
                    self.counter += 1
        return self.counter
    
    # Look up, down, left, and right
    def recurse(self, i, j):
        if i < 0 or i >= len(self.grid): # Out of range checks
            return
        if j < 0 or j >= len(self.grid[i]):
            return
        
        if self.grid[i][j] == "1":
            self.grid[i][j] = "0"
            self.recurse(i+1, j)
            self.recurse(i-1, j)
            self.recurse(i, j+1)
            self.recurse(i, j-1)
        
        return