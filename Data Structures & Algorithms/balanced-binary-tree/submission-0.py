# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        returnValue = True
        
        def dfs(root):
            if root == None:
                return 0

            L = dfs(root.left)
            R = dfs(root.right)
            
            print(root.val, L, R)
            if abs(L - R) > 1:
                nonlocal returnValue
                returnValue = False
            
            return max(L, R) + 1

        dfs(root)
        
        return returnValue
