class Solution:
    def __init__(self):
        self.val = None
        self.depth = None
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.value = val
        self.depth = depth
        if depth == 1:
            return TreeNode(val, root)
        return self.updateDepthLevelTree(root, 1)

    def updateDepthLevelTree(self, root, currentDepth):
        if currentDepth == (self.depth - 1) and root:
            left, right = root.left, root.right
            root.left, root.right = TreeNode(self.value, left), TreeNode(self.value, None, right)
            return root
        currentDepth += 1

        if root:
            self.updateDepthLevelTree(root.left, currentDepth)
            self.updateDepthLevelTree(root.right, currentDepth)

        return root