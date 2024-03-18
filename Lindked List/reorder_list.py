# Definition for singly-linked list.
import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        second_head = None
        i = 1
        temp = head.next
        while temp is not None:
            temp = temp.next
            i += 1
        mid = math.ceil(i / 2)
        temp = head
        i = 1
        while True:
            if i == mid:
                second_head = temp.next
                temp.next = None
                break
            temp = temp.next
            i += 1
        second_head = self.recursionRevers(second_head)
        temp1 = head
        temp2 = second_head
        while True:
            temp4 = temp2.next
            temp3 = temp1.next
            temp1.next = temp2
            temp2.next = temp3
            if temp4 is None:
                return
            temp2 = temp4
            temp1 = temp3
        """
        Do not return anything, modify head in-place instead.
        """

    def recursionRevers(self, node):
        if node.next is None:
            return node
        else:
            temp = node.next
            new_head = self.recursionRevers(node.next)
            temp.next = node
            node.next = None
            return new_head

    def fillLinkedList(self, list):
        head = ListNode(list[0])
        temp = head
        for i in range(1, len(list)):
            temp.next = ListNode(list[i])
            temp = temp.next
        return head


s = Solution()

head1 = s.fillLinkedList(list=[1, 2, 3, 4, 5])

s.reorderList(head1)

print(head1.val)
