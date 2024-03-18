import queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    answer = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.recursionTree(p, q)

    def recursionTree(self, branch1, branch2):
        if branch1 is None:
            if branch2 is None:
                return True
            else:
                return False
        else:
            if branch2 is None:
                return False
        if branch1.val != branch2.val:
            return False
        a1 = self.recursionTree(branch1.left, branch2.left)
        a2 = self.recursionTree(branch1.right, branch2.right)
        return a2 and a1

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
p = s.getRoot([1, 3])
q = s.getRoot([1, 3])
print(s.isSameTree(p, q))
