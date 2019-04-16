# 只能使用list的append和pop(-1)函数
class Queue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, value):
        self.stack_1.append(value)

    def dequeue(self):
        if self.stack_2:
            return self.stack_2.pop(-1)
        else:
            if not self.stack_1:
                return -1
            else:
                while self.stack_1:
                    self.stack_2.append(self.stack_1.pop(-1))
            return self.stack_2.pop(-1)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())