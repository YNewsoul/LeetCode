class Node:
    """一个双向链表节点"""

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 使用哈希表存储节点，便于快速访问
        self.head = Node(0, 0)  # 头节点，不存储实际的key和value
        self.tail = Node(0, 0)  # 尾节点，不存储实际的key和value
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            # 返回前要将节点移动到头部
            # 先删除
            self._delete_node(self.cache[key])
            # 再添加到头部
            self._add_to_head(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 情况1：key存在
            self.cache[key].value = value
            # 先删除
            self._delete_node(self.cache[key])
            # 再添加到头部
            self._add_to_head(self.cache[key])
        else:
            # 情况2：key不存在
            node = Node(key, value)
            self.cache[key] = node  # 将新节点添加到哈希表中
            self._add_to_head(node)  # 将新节点添加到头部
            self.size += 1
            if self.size > self.capacity:
                # 删除尾节点
                node = self._delete_tail()
                self.cache.pop(node.key)  # 从哈希表中删除节点
                self.size -= 1

    def _delete_node(self, node: Node):
        """删除双向链表中的节点"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node: Node):
        node.next = self.head.next  # 新节点指向头节点的下一个节点
        self.head.next.prev = node  # 头节点的下一个节点的前驱指向新节点
        self.head.next = node  # 新节点指向头节点
        node.prev = self.head  # 新节点的前驱指向头节点

    def _delete_tail(self) -> Node:
        """删除尾节点"""
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node
