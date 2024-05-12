"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        answer = Node(node.val)
        my_dict = {node.val: answer}
        self.rec_help(node, my_dict)
        return answer

    def rec_help(self, node, my_dict):
        for n in node.neighbors:
            if not n.val in my_dict:
                temp = Node(n.val)
                my_dict[n.val] = temp
                my_dict[node.val].neighbors.append(temp)
                self.rec_help(n, my_dict)
            else:
                if not my_dict[n.val] in my_dict[node.val].neighbors:
                    my_dict[node.val].neighbors.append(my_dict[n.val])


s = Solution()
firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)
fourNode = Node(4)
firstNode.neighbors.append(secondNode)
firstNode.neighbors.append(fourNode)
secondNode.neighbors.append(firstNode)
secondNode.neighbors.append(thirdNode)
thirdNode.neighbors.append(secondNode)
thirdNode.neighbors.append(fourNode)
fourNode.neighbors.append(firstNode)
fourNode.neighbors.append(thirdNode)
ans = s.cloneGraph(firstNode)
print()
