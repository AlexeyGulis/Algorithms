import queue
from typing import Optional

from input.list_to_tree import TreeNode, get_root


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        my_queue = queue.Queue()
        my_queue.put([root, None, None])
        while True:
            if my_queue.empty():
                break
            temp = my_queue.get()
            if temp[0].left is not None:
                if temp[1] is None:
                    if temp[0].left.val >= temp[0].val:
                        return False
                    my_queue.put([temp[0].left, None, temp[0].val])
                else:
                    if temp[0].left.val >= temp[0].val or temp[0].left.val <= temp[1]:
                        return False
                    my_queue.put([temp[0].left, temp[1], temp[0].val])

            if temp[0].right is not None:
                if temp[2] is None:
                    if temp[0].right.val <= temp[0].val:
                        return False
                    if temp[1] is None:
                        my_queue.put([temp[0].right, temp[0].val, None])
                else:
                    if temp[0].right.val <= temp[0].val or temp[0].right.val >= temp[2]:
                        return False
                    my_queue.put([temp[0].right, temp[0].val, temp[2]])
        return True


s = Solution()
print(s.isValidBST(get_root([5, 1, 4, None, None, 3, 6])))
