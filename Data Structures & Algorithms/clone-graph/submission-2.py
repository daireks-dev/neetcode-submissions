"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        def dfs(node):
            #No need for visited set. Use the oldToNew set
            #Return to prevent need for second loop
            if node in oldToNew:
                return oldToNew[node]
            
            #No need for conditional when each visited node is unique
            copy = Node(node.val)
            oldToNew[node] = copy
            
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        dfs(node)
        return oldToNew[node]
            