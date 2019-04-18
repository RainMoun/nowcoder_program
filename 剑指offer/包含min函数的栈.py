class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, n):
        self.stack.append(n)
        if not self.min_stack or self.min_stack[-1] > n:
            self.min_stack.append(n)

    def pop(self):
        n = self.stack.pop()
        if self.min_stack and n == self.min_stack[-1]:
            self.min_stack.pop()


stack_1 = MinStack()
stack_1.push(3)
stack_1.push(5)
stack_1.push(1)
stack_1.pop()
print(stack_1.min_stack[-1])
