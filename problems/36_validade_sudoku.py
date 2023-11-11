class Solution:
    @staticmethod
    def validate_sodoku_list(sudoku_list: list[str]):
        n_count = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        for n in sudoku_list:
            if n == '.':
                continue

            n_val = n_count.get(n)
            if n_val is not None:
                if n_val > 0:
                    print(sudoku_list)
                    return False
                n_count[n] += 1
            else:
                print(sudoku_list)
                return False
            
        return True
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            # validate line
            if not Solution.validate_sodoku_list(board[i]):
                return False
            
            # validate row
            row = [line[i] for line in board]
            if not Solution.validate_sodoku_list(row):
                return False
            
        # validating boxes
        for i in range(3):
            lines = board[i*3:(i+1)*3]
            for j in range(3):
                box = lines[0][j*3:(j+1)*3] + lines[1][j*3:(j+1)*3] + lines[2][j*3:(j+1)*3]
                
                if not Solution.validate_sodoku_list(box):
                    return False

        return True
