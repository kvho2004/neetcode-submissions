# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            if p is None and q is None:
                return True
            if p is None and q:
                return False
            if q is None and p:
                return False
            
            if p.val != q.val:
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p,q)
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:     
        if not subRoot:
            return True
        
        if not root:
            return False



        
        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            

        