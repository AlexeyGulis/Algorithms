import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_root(my_list):
    my_queue = queue.Queue()
    root = None
    if len(my_list) != 0:
        i = 0
        while True:
            if len(my_list) == i:
                break
            if i == 0:
                root = TreeNode(my_list[i])
                my_queue.put(root)
            else:
                temp = my_queue.get()
                if my_list[i] is not None:
                    temp.left = TreeNode(my_list[i])
                    my_queue.put(temp.left)
                else:
                    temp.left = None

                if i + 1 == len(my_list):
                    break
                else:
                    i += 1

                if my_list[i] is not None:
                    temp.right = TreeNode(my_list[i])
                    my_queue.put(temp.right)
                else:
                    temp.right = None
            i += 1
    return root
