# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def search(root):
            if not root:
                return

            left = search(root.left)
            if left:
                return left

            self.count += 1
            if self.count == k:
                return root

            return search(root.right)

        return search(root).val
        


        
        