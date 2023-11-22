class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)

        # if the _min_stack is empty
        # or the new value is smaller or equal to the current min
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        output = self._stack.pop()
        if output == self._min_stack[-1]:
            self._min_stack.pop()

        return output

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]
