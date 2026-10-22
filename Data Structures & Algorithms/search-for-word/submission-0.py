class Solution:
    """
    board = [
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ],
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.board = board
        self.found = False
        self.max_height = len(board[0])
        self.max_width = len(board)
        self.master_dictionary = {}

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                lst = tuple([i, j])
                self.master_dictionary[lst] = 0

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                self.recurse(i, j, 0)
        
        return self.found

    # This step checks and recurses to the next step IF we
    # can find a character from word and move on to the next.
    def recurse(self,
        i: int, # x-coordinate
        j: int, # y-coordinate
        index: int, # Index for the current character we are looking at from `word`
    ):
        accessed_ch = self.master_dictionary
        # Initial hard checks:
        if i < 0 or i >= self.max_width or j < 0 or j >= self.max_height:
            return

        ch = self.board[i][j]
        if ch != self.word[index]:
            return
        
        if accessed_ch[i, j] == 1:
            return
        
        # Check if we succeeded.
        if index == len(self.word) - 1:
            self.found = True
            return

        
        # We can successfully move forward. The current character is valid.
        accessed_ch[i, j] = 1

        left = [i-1, j]
        right = [i+1, j]
        up = [i, j-1]
        down = [i, j+1]

        self.recurse(left[0], left[1], index+1)
        self.recurse(right[0], right[1], index+1)
        self.recurse(up[0], up[1], index+1)
        self.recurse(down[0], down[1], index+1)

        accessed_ch[i, j] = 0