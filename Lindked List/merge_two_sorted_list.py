from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        head = None
        prev_list = None
        while temp1 is not None or temp2 is not None:
            if head is None:
                if temp1 is None:
                    head = temp2
                    prev_list = head
                    temp2 = temp2.next
                    continue
                if temp2 is None:
                    head = temp1
                    prev_list = head
                    temp1 = temp1.next
                    continue
                if temp1.val > temp2.val:
                    head = temp2
                    prev_list = head
                    temp2 = temp2.next
                else:
                    head = temp1
                    prev_list = head
                    temp1 = temp1.next
            else:
                if temp1 is None:
                    prev_list.next = temp2
                    prev_list = temp2
                    temp2 = temp2.next
                    continue
                if temp2 is None:
                    prev_list.next = temp1
                    prev_list = temp1
                    temp1 = temp1.next
                    continue
                if temp1.val > temp2.val:
                    prev_list.next = temp2
                    prev_list = temp2
                    temp2 = temp2.next
                else:
                    prev_list.next = temp1
                    prev_list = temp1
                    temp1 = temp1.next


        return head

    def fillLinkedList(self, list):
        head = ListNode(list[0])
        temp = head
        for i in range(1, len(list)):
            temp.next = ListNode(list[i])
            temp = temp.next
        return head


s = Solution()

head1 = s.fillLinkedList(list=[1, 2, 4])
head2 = s.fillLinkedList(list=[1, 3, 4])
head = s.mergeTwoLists(head1, head2)

print(head.val)
