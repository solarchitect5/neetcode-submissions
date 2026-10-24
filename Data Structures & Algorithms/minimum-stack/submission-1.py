class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, input_value: int) -> None:
        self.stack.append(input_value)
        input_value = min(input_value, self.minStack[-1] if self.minStack else input_value)
        self.minStack.append(input_value)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]