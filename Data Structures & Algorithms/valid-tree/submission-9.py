class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Create adj list
        neighbors = {i:[] for i in range(n)}
        for curr, nxt in edges:
            neighbors[curr].append(nxt)
            neighbors[nxt].append(curr)
        
        #Check if connected graph
        visited = set()
        def dfs(curr):
            if curr in visited:
                return
            
            visited.add(curr)

            for n in neighbors[curr]:
                dfs(n)
    
        dfs(0)
        return len(visited) == n and len(edges) == n-1