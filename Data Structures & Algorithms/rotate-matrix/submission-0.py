class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(r, COLS):
                if r == c:
                    continue
                else:
                    temp = matrix[r][c]
                    matrix[r][c] = matrix[c][r]
                    matrix[c][r] = temp
        
        for r in range(ROWS):
            for c in range(int(COLS/2)):
                temp = matrix[r][c]
                matrix[r][c] = matrix[r][COLS - 1 - c]
                matrix[r][COLS - 1 - c] = temp
