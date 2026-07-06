# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.largestDepth = 0
        def traverse(root, currentDepth):
            if not root:
                return
            self.largestDepth = max(currentDepth, self.largestDepth)
            traverse(root.left, currentDepth + 1)
            traverse(root.right, currentDepth + 1)
        traverse(root, 1)

        return self.largestDepth