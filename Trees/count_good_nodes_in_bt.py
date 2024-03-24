import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        my_queue = queue.Queue()
        my_queue.put([root, root.val])
        answer = 1
        while True:
            if my_queue.empty():
                break
            temp = my_queue.get()
            if temp[0].left is not None:
                if temp[0].left.val >= temp[1]:
                    answer += 1
                my_queue.put([temp[0].left, max(temp[1], temp[0].left.val)])
            if temp[0].right is not None:
                if temp[0].right.val >= temp[1]:
                    answer += 1
                my_queue.put([temp[0].right, max(temp[1], temp[0].right.val)])
        return answer

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
print(s.goodNodes(s.getRoot([1])))
