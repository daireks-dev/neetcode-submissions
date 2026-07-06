from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                
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
            
