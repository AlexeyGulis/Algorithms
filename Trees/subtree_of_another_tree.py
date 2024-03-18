import queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        my_queue = queue.Queue()
        my_queue.put(root)
        while True:
            if my_queue.empty():
                break
            temp = my_queue.get()
            if temp.val == subRoot.val:
                if self.isSameTree(temp, subRoot):
                    return True
            if temp.left is not None:
                my_queue.put(temp.left)
            if temp.right is not None:
                my_queue.put(temp.right)
        return False

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
root = s.getRoot([3, 4, 5, 1, 2])
sub_root = s.getRoot([4, 1, 2])
print(s.isSubtree(root, sub_root))
