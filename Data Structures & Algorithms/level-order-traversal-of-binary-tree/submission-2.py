# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        res = []
        queue = deque([(root, 0)])
        
        while queue:
            node, depth = queue.popleft()

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

            if len(res) == depth:
                res.append([node.val])
            else:
                res[depth].append(node.val)

        return res

        
            


