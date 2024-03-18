import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    p1 = None
    q1 = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = self.recursionTree(root, p.val, q.val)
        return answer

    def recursionTree(self, branch, val_p, val_q):
        if branch is None:
            return None
        a1 = self.recursionTree(branch.left, val_p, val_q)
        a2 = self.recursionTree(branch.right, val_p, val_q)
        if a1 is not None and a2 is not None:
            return branch
        if a1 is None:
            if a2 is None:
                if branch.val == val_p or branch.val == val_q:
                    return branch
                return None
            else:
                if branch.val == val_p or branch.val == val_q:
                    return branch
                return a2
        else:
            if branch.val == val_p or branch.val == val_q:
                return branch
            return a1

    def getRoot(self, list, p_val, q_val):
        my_queue = queue.Queue()
        root = None
        if len(list) != 0:
            i = 0
            while True:
                if len(list) == i:
                    break
                if i == 0:
                    root = TreeNode(list[i])
                    if list[i] == p_val:
                        self.p1 = root
                    if list[i] == q_val:
                        self.q1 = root
                    my_queue.put(root)
                else:
                    temp = my_queue.get()
                    if list[i] is not None:
                        temp.left = TreeNode(list[i])
                        if list[i] == p_val:
                            self.p1 = temp.left
                        if list[i] == q_val:
                            self.q1 = temp.left
                        my_queue.put(temp.left)
                    else:
                        temp.left = None

                    if i + 1 == len(list):
                        break
                    else:
                        i += 1

                    if list[i] is not None:
                        temp.right = TreeNode(list[i])
                        if list[i] == p_val:
                            self.p1 = temp.right
                        if list[i] == q_val:
                            self.q1 = temp.right
                        my_queue.put(temp.right)
                    else:
                        temp.right = None
                i += 1
        return root


s = Solution()
root = s.getRoot([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 6)
print(s.lowestCommonAncestor(root, s.p1, s.q1).val)
