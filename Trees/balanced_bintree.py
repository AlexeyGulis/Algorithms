from typing import Optional
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

    def getRoot(self, list):
        my_queue = queue.Queue()
        root = None
        if len(list) != 0:
            i = 0
            while True:
                if len(list) == i:
                    break
                if i == 0:
                    root = TreeNode(list[i])
                    my_queue.put(root)
                else:
                    temp = my_queue.get()
                    if list[i] is not None:
                        temp.left = TreeNode(list[i])
                        my_queue.put(temp.left)
                    else:
                        temp.left = None

                    if i + 1 == len(list):
                        break
                    else:
                        i += 1

                    if list[i] is not None:
                        temp.right = TreeNode(list[i])
                        my_queue.put(temp.right)
                    else:
                        temp.right = None
                i += 1
        return root


s = Solution()
root = s.getRoot([3, 9, 20, None, None, 15, 7])
print(s.isBalanced(root))
