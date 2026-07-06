
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Both nodes are null
        if not p and not q:
            return True
        #One node is null another has a val
        if not p or not q:
            return False
        #Values don't match:
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
            
            
