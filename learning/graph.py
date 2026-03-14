from collections import deque
# 图


# DFS遍历
# 一条路走到黑
def dfs(graph, start, visited=None):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# BFS遍历
# 用双向队列来实现
def bds(graph, start):
    visited = set([start])
    q = deque([start])
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


import heapq


def dijkstra(graph, start):
    """
    graph: 图（字典）
         key: 节点
         value: list [(邻居, 权重)]
    start: 起点
    return: 从 start 到所有点的最短距离
    """
    # 1. 初始化距离：所有点默认为无穷大
    dist = {node: float("inf") for node in graph}
    dist[start] = 0  # 起点到自己距离 = 0

    # 2. 最小堆（优先队列）
    # 堆里存 (距离, 节点)
    heap = []
    heapq.heappush(heap, (0, start))

    # 3. 开始贪心松弛
    while heap:
        current_dist, u = heapq.heappop(heap)  # 取距离最小的点

        # 优化：如果已经有更短距离，跳过旧数据
        if current_dist > dist[u]:
            continue

        # 遍历邻居
        # 遍历 u 的所有邻居 v
        for v, weight in graph[u]:
            # 松弛操作：如果通过 u 到 v 更短，更新距离
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))
    return dist
