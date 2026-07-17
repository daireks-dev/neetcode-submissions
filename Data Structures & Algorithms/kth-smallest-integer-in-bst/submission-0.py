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

            found = search(root.left)
            if found:
                return found

            self.count += 1
            if self.count == k:
                return root

            found = search(root.right)
            if found:
                return found

        return search(root).val
        


        
        