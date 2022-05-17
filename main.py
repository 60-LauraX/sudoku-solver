from sudoku import Solver

class Main:
    def main():
        solver = Solver()
        board = []
        print("Enter elements of sudoku puzzle per line separated by space")
        print("Fill empty space with 0")
        for i in range(9):
            row = [int(x) for x in input().strip().split()]
            board.append(row)
        print()
        solver.solveSudoku(board)
