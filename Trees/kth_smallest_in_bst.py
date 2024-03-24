import queue
from typing import Optional

from input.list_to_tree import TreeNode, get_root


class Solution:
    answer = 0
    index = 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.recursion_tree(root, k)
        return self.answer

    def recursion_tree(self, branch, k):

        if branch.left is not None:
            self.recursion_tree(branch.left, k)
        if self.index == k:
            self.answer = branch.val
        self.index += 1
        if self.index > k:
            return
        if branch.right is not None:
            self.recursion_tree(branch.right, k)


s = Solution()

print(s.kthSmallest(get_root([3, 1, 4, None, 2]), 1))
