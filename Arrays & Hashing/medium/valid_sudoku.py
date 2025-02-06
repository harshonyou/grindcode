from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        block, row, col = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if (
                        board[i][j] in row[i]
                        or board[i][j] in col[j]
                        or board[i][j] in block[(i // 3, j // 3)]
                    ):
                        return False
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    block[(i // 3, j // 3)].add(board[i][j])
        return True
