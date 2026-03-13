class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # 注意：self.head和self.tail是哨兵节点，不存储实际的key和value
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        # 情况1：key不存在
        if key not in self.cache:
            return -1
        # 情况2：key存在
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 情况1：key不存在
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                # 删除尾节点
                key = self._delete_tail()
                self.cache.pop(key)
                self.size -= 1
        else:
            # 情况2：key存在
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)

    # 移动到头部
    def _move_to_head(self, node: Node) -> None:
        # 先删除再移动
        self._delete_node(node)
        self._add_to_head(node)

    def _delete_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _delete_tail(self) -> int:
        node = self.tail.prev
        self._delete_node(node)
        return node.key

    def _add_to_head(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
