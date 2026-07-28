class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            adjList[p].append(c)
        
        #A global visited works as it backtracks within the dfs function
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

            #Instead of maintaining a second set. Represent completion with an empty array for future calls to reference
            adjList[c] = []

            return True
        
        #Iterate through every node in the case the graph is not connected.
        for i in range(numCourses):
            if dfs(i) == False:
                return False

        return True

        