class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def dfs(pos):
            if (min(pos[0], pos[1]) < 0 or
                pos[0] >= len(grid) or pos[1] >= len(grid[0]) or
                pos in visited or grid[pos[0]][pos[1]] == "0"):
                return
            
            visited.add((pos[0], pos[1]))
            
            dfs((pos[0] + 1, pos[1]))
            dfs((pos[0] - 1, pos[1]))
            dfs((pos[0], pos[1] + 1))
            dfs((pos[0], pos[1] - 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not (i, j) in visited:
                    dfs((i, j))
                    islands += 1
        
        return islands


                