class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        visited = set()
        def dfs(node):
            visited.add(node)

            for neighbor in adjList[node]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
            
        count = 0
        for node in range(n):
            if not node in visited:
                dfs(node)
                count += 1
        return count