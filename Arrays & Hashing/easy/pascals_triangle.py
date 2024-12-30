class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        rows = [[1], [1, 1]]

        if numRows <= 2:
            return rows[:numRows]

        for i in range(2, numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = rows[i - 1][j] + rows[i - 1][j - 1]
            rows.append(row)

        return rows
