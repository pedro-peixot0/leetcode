from typing import Optional

class Solution:
    @staticmethod
    def find_possible_numbers(board, current_i, current_j):
        options = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        row = board[current_i]
        column = [row[current_j] for row in board]

        start_box_i = (current_i // 3) * 3
        start_box_j = (current_j // 3) * 3
        box = board[start_box_i+0][start_box_j:start_box_j+3] +\
              board[start_box_i+1][start_box_j:start_box_j+3] +\
              board[start_box_i+2][start_box_j:start_box_j+3]

        return options - set(row + column + box)

    def solveSudoku(self, board: list[list[str]]) -> None:
        def recursive_solve() -> Optional[bool]:
            nonlocal board

            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        number_options = Solution.find_possible_numbers(board, i, j)

                        for number in number_options:
                            board[i][j] = number
                            if recursive_solve():
                                return True
                            else:
                                board[i][j] = '.'

                        return False

            return True

        recursive_solve()
        return board
