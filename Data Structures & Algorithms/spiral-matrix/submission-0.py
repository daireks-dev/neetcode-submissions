class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        pos = [0, -1]
        dirIndex = 0
        res = []

        while ROWS != 0 and COLS != 0:
            for i in range(COLS):
                pos[0] += DIR[dirIndex % 4][0]
                pos[1] += DIR[dirIndex % 4][1]
                res.append(matrix[pos[0]][pos[1]])
            ROWS -= 1
            dirIndex += 1
            
            for j in range(ROWS):
                pos[0] += DIR[dirIndex % 4][0]
                pos[1] += DIR[dirIndex % 4][1]
                res.append(matrix[pos[0]][pos[1]])
            COLS -= 1
            dirIndex += 1
        
        return res
    