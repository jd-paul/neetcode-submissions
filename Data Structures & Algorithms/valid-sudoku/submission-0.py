class Solution:
    """
    [["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check for duplicates for each row
        for row in board:
            lst = []
            for cell in row:
                if cell.isnumeric():
                    if cell not in lst:
                        lst.append(cell)
                    else:
                        return False
        
        # Check for duplicates in each column
        for i in range(0, 9):
            lst = []
            for j in range(0, 9):
                cell = board[j][i]
                if cell.isnumeric():
                    if cell not in lst:
                        lst.append(cell)
                    else:
                        return False
        
        """
        Each of the nine 3 x 3 sub-boxes of the grid must
        contain the digits 1-9 without duplicates.
        """

        groups = [
            # Box A
            [
                board[0][0:3], board[1][0:3], board[2][0:3]
            ],
            # Box B
            [
                board[0][3:6], board[1][3:6], board[2][3:6]
            ],
            # Box C
            [
                board[0][6:9], board[1][6:9], board[2][6:9]
            ],
            # Box D
            [
                board[3][0:3], board[4][0:3], board[5][0:3]
            ],
            # Box E
            [
                board[3][3:6], board[4][3:6], board[5][3:6]
            ],
            # Box F
            [
                board[3][6:9], board[4][6:9], board[5][6:9]
            ],
            # Box G
            [
                board[6][0:3], board[7][0:3], board[8][0:3]
            ],
            # Box H
            [
                board[6][3:6], board[7][3:6], board[8][3:6]
            ],
            # Box I
            [
                board[6][6:9], board[7][6:9], board[8][6:9]
            ],
        ]

        # Check for duplicates in each group
        """
        box = [
            [0][0:3], [1][0:3], [2][0:3]
        ],

        [
            List, List, List
        ]
        """
        for box in groups:
            lst = []
            for inner_lst in box:
                for cell in inner_lst:
                    if cell.isnumeric():
                        if cell not in lst:
                            lst.append(cell)
                        else:
                            return False
        
        return True
