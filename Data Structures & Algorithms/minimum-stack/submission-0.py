class MinStack:
    stack: list
    curr_min: list
    curr_min_len: int

    def __init__(self):
        self.stack = []
        self.curr_min = []
        self.curr_min_len = 0

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.curr_min_len == 0:
            self.curr_min.append(val)
            self.curr_min_len += 1
        else:
            tmp = self.curr_min[-1]
            self.curr_min.append(min(val, tmp))
            self.curr_min_len += 1

    def pop(self) -> None:
        self.stack.pop()
        self.curr_min.pop()
        self.curr_min_len -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min[-1]
