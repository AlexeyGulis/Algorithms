from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        self.recursInvert(root)
        return root

    def recursInvert(self, branch):
        if branch is None:
            return
        temp = branch.left
        branch.left = branch.right
        branch.right = temp
        self.recursInvert(branch.left)
        self.recursInvert(branch.right)
