# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def In(root,arr):   
            if root is None:
                return 
            else:
                In(root.left,arr)
                arr.append(root.val)
                In(root.right,arr)
            return arr
        return In(root,[])     