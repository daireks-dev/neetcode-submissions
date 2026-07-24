class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        newBoard = [[None for j in range(0, len(board[0]) + 2)] for i in range(0, len(board) + 2)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                newBoard[i+1][j+1] = board[i][j]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(index, position, visited):
            if newBoard[position[0]][position[1]] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            
            for d in directions:
                nextPosition = (position[0] + d[0], position[1] + d[1])
                nextChar = newBoard[nextPosition[0]][nextPosition[1]]

                if not nextPosition in visited and nextChar:
                    visited.add(nextPosition)

                    if dfs(index + 1, nextPosition, visited):
                        return True

                    visited.remove(nextPosition)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(0, (i+1, j+1), set([(i+1, j+1)])):
                    return True

        return False



