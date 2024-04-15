# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,path):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                ans += path*10 +node.val
                return
            dfs(node.left, path*10 + node.val)
            dfs(node.right, path*10 + node.val)
            
        ans = 0
        dfs(root,0)
        return ans
            