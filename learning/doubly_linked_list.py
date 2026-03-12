# 双向链表
# 包括自定义的实现方式 + python自带库


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 在尾部追加节点
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last

    # 在头部追加节点
    def prepend(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # 删除指定节点

    def delete_node(self, key):
        current = self.head
        while current:
            if current.val == key:
                # 情况1：要删的是头节点
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                # 情况2：要删的是中间/尾部节点
                else:
                    if current.next:
                        current.next.prev = current.prev
                    current.prev.next = current.next
                return
            current = current.next


# # python 双向链表 deque
from collections import deque

# 创建
d = deque([1, 2, 3])

d.appendleft(0)  # 左边加
d.append(4)  # 右边加
print(d)  # deque([0,1,2,3,4])

d.popleft()  # 删左边
d.pop()  # 删右边
print(d)  # deque([1,2,3])

# 反向遍历
for x in reversed(d):
    print(x)  # 3 2 1


## 有序字典+双向链表
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
# 把a移动到最后
od.move_to_end("a")  #
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])
# 把b移动到最前
od.move_to_end("b", last=False)
print(od)  # OrderedDict([('b', 2), ('a', 1), ('c', 3)])

od.popitem()  # 删除最后一个
print(od)  # OrderedDict([('b', 2), ('a', 1)])

od.popitem(last=False)  # 删除最前一个
print(od)  # OrderedDict([('a', 1)])
