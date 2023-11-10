class MyQueue:
    def __init__(self):
        self.stack_1 = [] # input
        self.stack_2 = [] # output

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stack_2.pop()
    def peek(self) -> int:
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())   

        return self.stack_2[-1]

    def empty(self) -> bool:
        return not (self.stack_1 or self.stack_2)
