class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        newBoard = [[None for j in range(0, len(board[0]) + 2)] for i in range(0, len(board) + 2)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                newBoard[i+1][j+1] = board[i][j]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(current, position, visited):
            if not current:
                return False
            if "".join(current) == word:
                return True
            
            for d in directions:
                nextPosition = (position[0] + d[0], position[1] + d[1])
                nextChar = newBoard[nextPosition[0]][nextPosition[1]]

                if not nextPosition in visited and nextChar:
                    visited.add(nextPosition)
                    current.append(nextChar)

                    if dfs(current, nextPosition, visited):
                        return True

                    visited.remove(nextPosition)
                    current.pop()
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs([board[i][j]], (i+1, j+1), set([(i+1, j+1)])):
                    return True

        return False



