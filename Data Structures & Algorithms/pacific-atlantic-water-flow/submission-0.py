from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Reaches pacific when r == -1 or c == -1
        #Reaches Atlantic when r == ROW or c == COL
        ROWS, COLS = len(heights), len(heights[0])

        def bfs(initRow, initCol):
            visited = set()
            queue = deque()
            visited.add((initRow, initCol))
            queue.append((initRow, initCol))

            reachesPacific = False
            reachesAtlantic = False
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in directions:
                        if r + dr < 0 or c + dc < 0:
                            reachesPacific = True
                            continue
                        if r + dr >= ROWS or c + dc >= COLS:
                            reachesAtlantic = True
                            continue
                        if ((r + dr, c + dc) in visited or
                            heights[r + dr][c + dc] > heights[r][c]):
                            continue
                        
                        visited.add((r + dr, c + dc))
                        queue.append((r + dr, c + dc))

            return reachesAtlantic and reachesPacific
        
        result = []
        for i in range(ROWS):
            for j in range(COLS):
                if bfs(i, j):
                    result.append([i, j])
        
        return result






            
            