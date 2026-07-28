class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            adjList[p].append(c)
        
        visited = set()
        def dfs(c):
            if c in visited:
                return False
            if adjList[c] == []:
                return True

            visited.add(c)
            for nei in adjList[c]:
                if dfs(nei) == False: 
                    return False
            visited.remove(c)
            adjList[c] = []

            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True

        