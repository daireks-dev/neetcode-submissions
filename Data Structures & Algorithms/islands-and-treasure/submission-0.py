from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(initRow, initCol):
            visited = set()
            queue = deque()
            visited.add((initRow, initCol))
            queue.append((initRow, initCol))

            dist = 0
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    if grid[r][c] == 0:
                        return dist
                
                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in directions:
                        if (min(r + dr, c + dc) < 0 or
                            r + dr >= ROWS or c + dc >= COLS or
                            (r + dr, c + dc) in visited or 
                            grid[r + dr][c + dc] == -1):
                            continue
                        
                        visited.add((r + dr, c + dc))
                        queue.append((r + dr, c + dc))
                dist += 1
            return INF
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i, j)