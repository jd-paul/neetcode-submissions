class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:                                    
        if not grid:                                                                                
            return                                                                                  
                                                                                                    
        rows, cols = len(grid), len(grid[0])                                                        
        INF = 2147483647                                                                            
        queue = deque()                                                                             
                                                                                                    
        # Start BFS from every treasure simultaneously.                                             
        for row in range(rows):                                                                     
            for col in range(cols):                                                                 
                if grid[row][col] == 0:                                                             
                    queue.append((row, col))                                                        
                                                                                                    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]                                             
                                                                                                    
        while queue:                                                                                
            row, col = queue.popleft()                                                              
                                                                                                    
            for dr, dc in directions:                                                               
                next_row = row + dr                                                                 
                next_col = col + dc                                                                 
                                                                                                    
                in_bounds = (                                                                       
                    0 <= next_row < rows                                                            
                    and 0 <= next_col < cols                                                        
                )                                                                                   
                                                                                                    
                # Water and already-visited cells are skipped.                                      
                if in_bounds and grid[next_row][next_col] == INF:                                   
                    grid[next_row][next_col] = grid[row][col] + 1                                   
                    queue.append((next_row, next_col))