class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []  # Tracks the minimum value at each level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty, or val is smaller/equal to current min, push it
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()  # Keep both stacks synchronized

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]