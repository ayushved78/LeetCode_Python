# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        #COPIED
        need = set()

        def search(node):
            if node:
                if node.val in need:
                    return True
                need.add(k-node.val)
                return search(node.left) or search(node.right)
                
        return search(root)