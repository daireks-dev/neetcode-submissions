class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefixSum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            currentSum = 0
            for j in range(cols):
                currentSum += matrix[i][j]
                aboveSum = self.prefixSum[i][j + 1]
                self.prefixSum[i + 1][j + 1] = currentSum + aboveSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topLeft = self.prefixSum[row1][col1]
        left = self.prefixSum[row2+1][col1] - topLeft
        top = self.prefixSum[row1][col2+1] - topLeft
        bottomRight = self.prefixSum[row2+1][col2+1]
        
        # Add back topLeft because it was subtracted twice
        return bottomRight - left - top - topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)