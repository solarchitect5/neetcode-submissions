
class Item:
    def __init__(self, prev=None, value=0, next=None) -> None:
        self.prev = prev
        self.value = value
        self.next = next

class MyStack:
    def __init__(self):
        self.head = Item()
        self.tail = Item()
        self.head.prev = self.tail 
        self.tail.next = self.head
        self.size = 0

    def push(self, value: int) -> None:
        new_item = Item(self.head.prev, value, self.head)      
        self.head.prev = new_item
        self.size += 1

    def pop(self) -> int:
        if not self.size:
            return
        pop_value = self.head.prev.value
        self.head = self.head.prev
        self.head.next = None
        self.size -= 1
        return pop_value

    def top(self) -> int:
        if (not self.size):
            return
        return self.head.prev.value

    def empty(self) -> bool:
        return (not self.size)
