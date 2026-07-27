class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        atlantic = set()
        pacific = set()
        
        #Pacific and Atlantic act as visited sets
        def dfs(curr, lastHeight, visited):
            if (min(curr[0], curr[1]) < 0 or 
            curr[0] >= ROWS or curr[1] >= COLS or
            curr in visited or lastHeight > heights[curr[0]][curr[1]]):
                return
            
            visited.add(curr)
            
            dfs((curr[0], curr[1] + 1), heights[curr[0]][curr[1]], visited)
            dfs((curr[0], curr[1] - 1), heights[curr[0]][curr[1]], visited)
            dfs((curr[0] + 1, curr[1]), heights[curr[0]][curr[1]], visited)
            dfs((curr[0] - 1, curr[1]), heights[curr[0]][curr[1]], visited)
        
        for i in range(0, COLS):
            dfs((ROWS-1, i), 0, atlantic)
        for i in range(0, ROWS):
            dfs((i, COLS-1), 0, atlantic)
        
        for i in range(0, COLS):
            dfs((0, i), 0, pacific)
        for i in range(0, ROWS):
            dfs((i, 0), 0, pacific)
        
        res = []
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])
        return res

            
        

