# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:
                return 0

            # compute the height of left and right subtrees
            lHeight = height(root.left)
            rHeight = height(root.right)

            return max(lHeight, rHeight) + 1

        ans = 0

        def dfs(curr):
            nonlocal ans
            if curr is None:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            path = left + right
            ans = max(ans, path)
            

            return 1 + max(left, right)

        dfs(root)
        return ans
