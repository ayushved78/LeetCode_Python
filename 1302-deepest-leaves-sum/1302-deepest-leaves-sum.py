# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        hm = {}
        self.dfs(root, 1, hm)
        return hm.get(max(hm.keys()))
    
    def dfs(self, node, height, hm):
        if node.left is None and node.right is None:
            if height in hm:
                hm[height] = hm[height] + node.val
            else:
                hm[height] = node.val
        else:
            if node.left is not None:
                self.dfs(node.left, height + 1, hm)
            if node.right is not None:
                self.dfs(node.right, height + 1,  hm)