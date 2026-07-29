class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Create adj list
        neighbors = {i:[] for i in range(n)}
        for curr, nxt in edges:
            neighbors[curr].append(nxt)
            neighbors[nxt].append(curr)
        
        #Check if connected graph
        visited = set()
        def dfs(curr, parent):
            visited.add(curr)

            for n in neighbors[curr]:
                if n == parent:
                    continue
                if n in visited:
                    return False
                if not dfs(n, curr):
                    return False
            
            return True
    
        dfs(0, -1)
        return len(visited) == n and len(edges) == n-1