from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        temp = head
        while True:
            if temp.next is None:
                temp.next = Node(temp.val)
                break
            temp2 = temp.next
            temp.next = Node(temp.val)
            temp.next.next = temp2
            temp = temp2
        temp = head
        while True:
            if temp.random is None:
                temp.next.random = None
            else:
                temp.next.random = temp.random.next
            if temp.next.next is None:
                break
            temp = temp.next.next
        temp = head
        new_head = head.next
        while True:
            if temp.next.next is None:
                temp.next = None
                break
            temp2 = temp.next
            temp.next = temp.next.next
            temp2.next = temp.next.next
            temp = temp.next
        return new_head

    def printList(self, head):
        temp = head
        my_s = ''
        while temp:
            my_s = my_s + str(temp.val) + ' -> '
            temp = temp.next
        print(my_s)
        my_s = ''
        temp = head
        while temp:
            out_s = ''
            if temp.random is None:
                out_s = out_s + 'None'
            else:
                out_s = out_s + str(temp.random.val)
            my_s = my_s + out_s + ' -> '
            temp = temp.next
        print(my_s)

    def fillLinkedList(self, list):
        my_list = []
        for i in range(len(list)):
            my_list.append(Node(list[i][0]))
        for i in range(len(my_list)):
            if i + 1 != len(my_list):
                my_list[i].next = my_list[i + 1]
            if list[i][1] is None:
                my_list[i].random = None
            else:
                my_list[i].random = my_list[list[i][1]]
        return my_list[0]


s = Solution()
head = s.fillLinkedList([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
s.printList(head)
new_copy_head = s.copyRandomList(head)
s.printList(new_copy_head)
