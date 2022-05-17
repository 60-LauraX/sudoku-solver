class Solver:
    def isValid(self, i, j, x, board):
        for col in range(9):
            if board[i][col] == x:
                return False
        
        for row in range(9):
            if board[row][j] == x:
                return False
        
        startrow = i-i%3
        startcol = j-j%3
        p = startrow
        while p <= startrow+2:
            l = startcol
            while l <= startcol+2:
                if board[p][l] == x:
                    return False
                l += 1
            p += 1
        
        return True

    def solveSudokuHelper(self, i, j, board):
        if i == 8 and j == 8:
            if board[i][j] != 0:
                for row in board:
                    for ele in row:
                        print(ele, end = " ")
                    print()
            else:
                for x in range(1, 10):
                    if self.isValid(i, j, x, board) is True:
                        board[i][j] = x
                        for row in board:
                            for ele in row:
                                print(ele, end = " ")
                            print()
                        board[i][j] = 0
            print()
            return
        
        if j > 8:
            self.solveSudokuHelper(i+1, 0, board)  
            return
        
        if board[i][j] == 0:
            for x in range(1, 10):
                if self.isValid(i, j, x, board) is True:
                    board[i][j] = x
                    self.solveSudokuHelper(i, j+1, board) 
                    board[i][j] = 0
        else:
            self.solveSudokuHelper(i, j+1, board)
        return

    def solveSudoku(self, board):
        print("Sudoku puzzle result")
        self.solveSudokuHelper(0, 0, board)
