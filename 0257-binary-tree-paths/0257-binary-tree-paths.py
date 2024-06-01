# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = str(root.val)
        def helper(node, res, path):
            if node.left:
                path_left = path + "->" + str(node.left.val)
                helper(node.left, res, path_left)
            if node.right:
                path_right = path + "->" + str(node.right.val)
                helper(node.right, res, path_right)
            if not node.right and not node.left:
                res.append(path)
        helper(root, res, path)
        return res