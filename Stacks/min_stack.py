# import queue
#
#
# class MinStack:
#
#     def __init__(self):
#         self.q1 = queue.LifoQueue()
#         self.q2 = queue.LifoQueue()
#
#     def push(self, val: int) -> None:
#         self.q1.put(val)
#         if self.q2.empty():
#             self.q2.put(val)
#         else:
#             p = self.q2.get()
#             self.q2.put(p)
#             if val <= p:
#                 self.q2.put(val)
#
#     def pop(self) -> None:
#         t1 = self.q1.get()
#         t2 = self.q2.get()
#         if t1 != t2:
#             self.q2.put(t2)
#
#     def top(self) -> int:
#         t1 = self.q1.get()
#         self.q1.put(t1)
#         return t1
#
#     def getMin(self) -> int:
#         t1 = self.q2.get()
#         self.q2.put(t1)
#         return t1

# Can make easy with array list

class Node:
    def __init__(self):
        self.prev = None
        self.prev_min = None
        self.next = None
        self.next_min = None
        self.val = None

    def getPrevMin(self):
        return self.prev_min

    def getPrev(self):
        return self.prev

    def getNextMin(self):
        return self.next_min

    def getNext(self):
        return self.next

    def getValue(self):
        return self.val

    def setPrev(self, prev):
        self.prev = prev

    def setPrevMin(self, prev_min):
        self.prev_min = prev_min

    def setNextMin(self, next_min):
        self.next_min = next_min

    def setNext(self, next):
        self.next = next

    def setValue(self, value):
        self.val = value


class MinStack:

    def __init__(self):
        self.last = None
        self.min = None

    def push(self, val: int) -> None:
        if self.last is None:
            node = Node()
            node.setValue(val)
            self.min = node
            self.last = node
        else:
            node = Node()
            node.setValue(val)
            if self.min.getValue() >= val:
                node.setPrevMin(self.min)
                self.min = node
            node.setPrev(self.last)
            self.last = node

    def pop(self) -> None:
        if self.last.getValue() == self.min.getValue():
            self.min = self.min.getPrevMin()
        self.last = self.last.getPrev()

    def top(self) -> int:
        return self.last.getValue()

    def getMin(self) -> int:
        return self.min.getValue()




minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
