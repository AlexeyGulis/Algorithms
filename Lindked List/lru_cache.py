class Node:
    def __init__(self, key, m_next, prev):
        self.key = key
        self.next = m_next
        self.prev = prev


class MyQueue:
    head = None
    tail = None

    def __init__(self):
        pass

    def removeHead(self) -> None:
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def addNode(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def moveToTail(self, node):
        if self.head == self.tail == node:
            return
        else:
            if self.tail == node:
                return
            if self.head == node:
                self.head = self.head.next
                self.head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


class LRUCache:
    CAPACITY = 0
    index = 0
    kv_dict = {}
    kn_dict = {}
    my_queue = None

    def __init__(self, capacity: int):
        self.index = 0
        self.CAPACITY = capacity
        self.my_queue = MyQueue()
        self.kv_dict = {}
        self.kn_dict = {}

    def get(self, key: int) -> int:
        if key in self.kv_dict:
            node = self.kn_dict[key]
            self.my_queue.moveToTail(node)
            return self.kv_dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.CAPACITY == self.index:
            if key in self.kv_dict:
                self.kv_dict[key] = value
                node = self.kn_dict[key]
                self.my_queue.moveToTail(node)
            else:
                self.kv_dict.pop(self.my_queue.head.key)
                self.kn_dict.pop(self.my_queue.head.key)
                self.my_queue.removeHead()
                self.kv_dict[key] = value
                node = Node(key, None, None)
                self.my_queue.addNode(node)
                self.kn_dict[key] = node
        else:
            if key not in self.kv_dict:
                self.index += 1
                node = Node(key, None, None)
                self.my_queue.addNode(node)
                self.kv_dict[key] = value
                self.kn_dict[key] = node
            else:
                self.kv_dict[key] = value
                node = self.kn_dict[key]
                self.my_queue.moveToTail(node)


lRUCache = None
answer = []
m1 = ["LRUCache","put","get"]
m2 = [[1],[2,1],[2]]
for i in range(len(m1)):
    if m1[i] == 'LRUCache':
        lRUCache = LRUCache(m2[i][0])
        answer.append(None)
    if m1[i] == 'put':
        answer.append(lRUCache.put(m2[i][0], m2[i][1]))
    if m1[i] == 'get':
        answer.append(lRUCache.get(m2[i][0]))

print(answer)
