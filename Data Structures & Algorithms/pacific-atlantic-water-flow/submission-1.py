class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        `heights` called via [y, x]
        Input: heights = [
            [4,2,7,3,4],
            [7,4,6,4,7],
            [6,3,5,3,6]
        ]
        """
        self.heights = heights
        self.pacific, self.atlantic = {}, {}
        self.heights_copy = []

        for lst in heights:
            self.heights_copy.append([0] * len(lst)) # If it's 0, we haven't traversed it yet.

        # Iterate through bottom-most and right-most

        height = len(heights)
        width = len(heights[0])
        for i in range(0, len(heights[0])): # Iterate through bottom-most
            self.recurse(i, height-1, "atlantic")

        for i in range(0, len(heights)): # Iterate through right-most
            self.recurse(width-1, i, "atlantic")
        
        for i in range(0, len(heights[0])): # Iterate through top-most
            self.recurse(i, 0, "pacific")
        
        for i in range(0, len(heights)): # Iterate through left-most
            self.recurse(0, i, "pacific")
        
        self.res = [
            [y, x]
            for (x, y) in self.pacific
            if (x, y) in self.atlantic
        ]
        return self.res
    
    def recurse(self, x: int, y: int, ocean: str): # i, j = x, y coordinate
        visited = self.pacific if ocean == "pacific" else self.atlantic

        rows = len(self.heights)
        cols = len(self.heights[0])
        
        if x < 0 or x >= cols or y < 0 or y >= rows:
            return

        if (x, y) in visited:
            return
        
        visited[(x, y)] = True

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0,-1)):
            nx, ny = x + dx, y + dy
        
            if 0 <= nx < cols and 0 <= ny < rows:
                if self.heights[ny][nx] >= self.heights[y][x]:
                    self.recurse(nx, ny, ocean)