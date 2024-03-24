from typing import Optional
from input.list_to_tree import TreeNode, get_root


class Solution:
    answer = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.recursionForTree(root, 0)
        return self.answer

    def recursionForTree(self, branch, depth):
        if branch is None:
            return depth
        a1 = self.recursionForTree(branch.left, depth + 1)
        a2 = self.recursionForTree(branch.right, depth + 1)
        if abs(a1 - a2) > 1:
            self.answer = False
        return max(a1, a2)


s = Solution()
root = get_root([3, 9, 20, None, None, 15, 7])
print(s.isBalanced(root))
