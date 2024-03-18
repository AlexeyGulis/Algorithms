from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        if head is None:
            return None
        new_head = self.recursionRevers(head)
        return new_head

    def recursionRevers(self, node):
        if node.next is None:
            return node
        else:
            temp = node.next
            new_head = self.recursionRevers(node.next)
            temp.next = node
            node.next = None
            return new_head


s = Solution()
test = [1,2,3,4,5]
head = ListNode(1)
temp = head
for i in range(1, len(test)):
    temp.next = ListNode(test[i])
    temp = temp.next

print(s.reverseList(head))
