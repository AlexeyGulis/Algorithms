from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    answer = 0
    my_depth = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.my_depth = self.recDepth(root, 0) - 1
        self.findDiam(root, 0)
        return self.answer

    def findDiam(self, branch, depth):
        s1 = self.my_depth - depth
        s2 = s1
        if branch.left is not None:
            s1 = self.findDiam(branch.left, depth + 1) + 1
        else:
            s1 = 0
        if branch.right is not None:
            s2 = self.findDiam(branch.right, depth + 1) + 1
        else:
            s2 = 0
        if self.answer < s1 + s2:
            self.answer = s1 + s2
        return max(s1, s2)

    # def findDiam(self, branch):
    #     a1 = 0
    #     a2 = 0
    #     if branch.left is not None:
    #         a1 = self.recDepth(branch.left, 0) + 1
    #         self.findDiam(branch.left)
    #     if branch.right is not None:
    #         a2 = self.recDepth(branch.right, 0) + 1
    #         self.findDiam(branch.right)
    #     if a1 + a2 > self.answer:
    #         self.answer = a1 + a2

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


s = Solution()

root = TreeNode(2, TreeNode(3, TreeNode(1)))
print(s.diameterOfBinaryTree(root))
