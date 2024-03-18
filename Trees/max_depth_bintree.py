from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0
        if root is None:
            return answer
        answer = self.recDepth(root, 0)
        return answer

    def recDepth(self, branch, depth):
        if branch is None:
            return depth
        new_depth = depth + 1
        a1 = self.recDepth(branch.left, new_depth)
        a2 = self.recDepth(branch.right, new_depth)
        if a1 > a2:
            return a1
        else:
            return a2