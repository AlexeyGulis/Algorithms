import queue
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        answer = {}
        my_queue = queue.Queue()
        i = 0
        my_queue.put([i, root])
        while True:
            if my_queue.empty():
                break
            temp = my_queue.get()
            if temp[0] in answer:
                answer[temp[0]].append(temp[1].val)
            else:
                answer[temp[0]] = [temp[1].val]
            if temp[1].left is not None:
                my_queue.put([temp[0] + 1, temp[1].left])
            if temp[1].right is not None:
                my_queue.put([temp[0] + 1, temp[1].right])
        return list(answer.values())

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

print(s.levelOrder(s.getRoot([3, 9, 20, None, None, 15, 7])))
