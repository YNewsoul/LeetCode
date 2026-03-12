class MinStack:
    def __init__(self):
        # 存储与最小值的差值
        self.stack = list()
        self.min_val = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val
            self.stack.append(0)
        else:
            diff = val - self.min_val
            if diff < 0:
                self.min_val = val
            self.stack.append(diff)

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            self.min_val -= diff

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min_val
        return self.min_val + self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
