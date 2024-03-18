from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        temp_node = head
        temp1 = temp_node.next
        temp2 = None
        temp_node.next = temp2
        while True:
            if temp1 is None:
                if temp_node == head:
                    return True
                break
            temp2 = temp_node
            temp_node = temp1
            temp1 = temp_node.next

            temp_node.next = temp2
        return False

    def printList(self, head, index):
        temp = head
        my_s = ''
        i = 0
        while temp:
            if i > index:
                break
            my_s = my_s + str(temp.val) + ' -> '
            temp = temp.next
            i += 1
        print(my_s)

    def fillLinkedList(self, list, pos):
        my_list = []
        for i in range(len(list)):
            my_list.append(ListNode(list[i]))
        for i in range(len(my_list)):
            if i + 1 != len(my_list):
                my_list[i].next = my_list[i + 1]
        if pos != -1:
            my_list[len(my_list) - 1].next = my_list[pos]
        return my_list[0]


s = Solution()

exc_list = [1]
head = s.fillLinkedList(exc_list, -1)

s.printList(head, len(exc_list))

print(s.hasCycle(head))
