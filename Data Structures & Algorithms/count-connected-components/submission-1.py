class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for curr, nxt in edges:
            adj[curr].append(nxt)
            adj[nxt].append(curr)   
        
        connected = 0
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return
            
            visited.add(node)

            for n in adj[node]:
                if n == prev:
                    continue
                dfs(n, node)
        
        for i in range(n):
            if not i in visited:
                dfs(i, -1)
                connected += 1

        return connected

