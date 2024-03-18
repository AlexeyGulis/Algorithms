from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        additional = 0
        if (l1.val + l2.val) // 10 == 0:
            new_head = ListNode(l1.val + l2.val)
            additional = 0
        else:
            new_head = ListNode((l1.val + l2.val) % 10)
            additional = 1
        t1 = l1.next
        t2 = l2.next
        t3 = new_head
        while True:
            if t1 is None and t2 is None:
                if additional == 1:
                    t3.next = ListNode(additional)
                break
            p1 = 0
            p2 = 0
            if t1 is not None:
                p1 = t1.val
                t1 = t1.next
            if t2 is not None:
                p2 = t2.val
                t2 = t2.next
            if (p1 + p2 + additional) // 10 == 0:
                t3.next = ListNode(p1 + p2 + additional)
                t3 = t3.next
                additional = 0
            else:
                t3.next = ListNode((p1 + p2 + additional) % 10)
                t3 = t3.next
                additional = 1
        return new_head

    def printList(self, head):
        temp = head
        my_s = ''
        while temp:
            my_s = my_s + str(temp.val) + ' -> '
            temp = temp.next
        print(my_s)

    def fillLinkedList(self, list):
        my_list = []
        for i in range(len(list)):
            my_list.append(ListNode(list[i]))
        for i in range(len(my_list)):
            if i + 1 != len(my_list):
                my_list[i].next = my_list[i + 1]
        return my_list[0]



s = Solution()

head1 = s.fillLinkedList([0])
head2 = s.fillLinkedList([0])

s.printList(head1)
s.printList(head2)

new_head = s.addTwoNumbers(head1, head2)

s.printList(new_head)