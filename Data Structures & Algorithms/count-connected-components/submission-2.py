class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for curr, nxt in edges:
            adj[curr].append(nxt)
            adj[nxt].append(curr)   
        
        connected = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for n in adj[node]:
                dfs(n)
        
        for i in range(n):
            if not i in visited:
                dfs(i)
                connected += 1

        return connected

