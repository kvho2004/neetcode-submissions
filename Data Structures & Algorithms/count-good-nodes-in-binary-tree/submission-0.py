# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(curr, maxValue):
            if not curr:
                return 0

            if curr.val >= maxValue:
                res = 1
            else:
                res = 0

            maxValue = max(maxValue, curr.val)
            res += dfs(curr.left, maxValue)
            res += dfs(curr.right, maxValue)
            return res

        return dfs(root, root.val)



            





            

