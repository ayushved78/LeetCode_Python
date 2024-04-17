# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = None
        a = ord('a')
        def dfs(node, path):
            nonlocal res, a            
            if not node:
                return    
            string = chr(node.val + a) + path
            if not node.left and not node.right:                
                if not res or string < res:
                    res = string
                return
            dfs(node.left, string)
            dfs(node.right, string)

        dfs(root, "")
        return res