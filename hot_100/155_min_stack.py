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


class MinStack_:
    def __init__(self):
        # 利用辅助栈一直维护当前最小值
        self.stack = []
        self.min_value_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_value_stack:
            # 栈不为空
            self.min_value_stack.append(min(val, self.min_value_stack[-1]))
        else:
            # 栈为空
            self.min_value_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_value_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value_stack[-1]
