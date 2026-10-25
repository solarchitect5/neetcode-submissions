class ListNode:
    def __init__(self, prev=None, value=0, next=None):
        self.prev = prev
        self.value = value
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = ListNode()          # Dummy Head
        self.tail = ListNode()          # Dummy Tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def getNode(self, index: int) -> ListNode:
        current_node = self.head.next
        for i in range(0, index):
            current_node = current_node.next
        return current_node

    def get(self, index: int):
        if index < 0 or index >= self.size:
            return -1
        return self.getNode(index).value

    def addAtHead(self, value: int) -> None:
        self.addAtIndex(0, value)

    def addAtTail(self, value: int) -> None:
        self.addAtIndex(self.size, value)

    def addAtIndex(self, index: int, value: int) -> None:
        if index < 0 or index > self.size:
            return
        current_node = self.getNode(index) if index < self.size else self.tail
        previous_node = current_node.prev
        new_node = ListNode(previous_node, value, current_node)
        previous_node.next = new_node
        current_node.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        current_node = self.getNode(index)
        previous_node = current_node.prev
        next_node = current_node.next
        previous_node.next = next_node
        next_node.prev = previous_node
        self.size -= 1
