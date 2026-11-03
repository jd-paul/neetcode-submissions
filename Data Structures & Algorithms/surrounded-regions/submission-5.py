class Solution:
    """
    visited = {} # Contains all visited coordinates 

    We do a two pass approach.

    First pass: Run a DFS on every 'O' on the border, marking them as '#'.

    Second pass: Traverse the matrix and convert cells matrix[i][j] == 'O' into 'X'

    We run a DFS on every 'O' on the border, marking them as '#' to
    avoid revisiting. After completing all DFS calls, we traverse the
    matrix again
    """
    def solve(self, board: List[List[str]]) -> None:
        self.board = board

        # First pass - Run a DFS on every 'O' on the border.
        visited = {} # First pass visited cells
        self.width, self.height = len(board[0]), len(board)

        for i in range(0, self.width): # Top row, left to right
            if self.board[0][i] == 'O' and tuple([0, i]) not in visited:
                self.dfs(0, i)
                visited[tuple([0, i])] = 1
        
        for i in range(0, self.width): # Bottom row, left to right
            if self.board[self.height-1][i] == 'O' and tuple([self.height-1, i]) not in visited:
                self.dfs(self.height-1, i)
                visited[tuple([self.height-1, i])] = 1
        
        for i in range(0, self.height): # Left column, top to bottom
            if self.board[i][0] == 'O' and tuple([i, 0]) not in visited:
                self.dfs(i, 0)
                visited[tuple([i, 0])] = 1
        
        for i in range(0, self.height): # Right column, top to bottom
            if self.board[i][self.width-1] == 'O' and tuple([i, self.width-1]) not in visited:
                self.dfs(i, self.width-1)
                visited[tuple([i, self.width-1])] = 1
        
        # Second pass - Convert all remaining 'O' as 'X', and convert '#' into O

        for i in range(0, self.width):
            for j in range(0, self.height):
                if self.board[j][i] == 'O':
                    self.board[j][i] = 'X'
                elif self.board[j][i] == '#':
                    self.board[j][i] = 'O'

    def dfs(self, i: int, j: int) -> None:
        # Out of bound checks
        if j < 0 or j >= self.width:
            return
        if i < 0 or i >= self.height:
            return
        if self.board[i][j] != 'O':
            return

        if self.board[i][j] == 'O':
            self.board[i][j] = '#'
        
        directions = [
            [0, 1], [0, -1],
            [1, 0], [-1, 0]
        ]

        for lst in directions:
            self.dfs(i + lst[0], j + lst[1])