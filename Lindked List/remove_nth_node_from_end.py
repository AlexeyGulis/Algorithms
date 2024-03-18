from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 1
        j = 1
        temp1 = head
        temp2 = head
        while True:
            if temp2.next is None:
                if j == n:
                    head = head.next
                    break
                temp1.next = temp1.next.next
                break
            j += 1
            temp2 = temp2.next
            if j - i - 1 == n:
                i += 1
                temp1 = temp1.next
        return head

    def fillLinkedList(self, list):
        head = ListNode(list[0])
        temp = head
        for i in range(1, len(list)):
            temp.next = ListNode(list[i])
            temp = temp.next
        return head

    def print(self, head):
        temp = head
        my_s = ''
        while temp:
            my_s = my_s + str(temp.val) + ' -> '
            temp = temp.next
        print(my_s)

s = Solution()
head = s.fillLinkedList([1,2,3,4,5])
s.print(head)
new_head = s.removeNthFromEnd(head, n=2)
s.print(new_head)
