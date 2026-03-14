from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        num_clen = len(prerequisites)
        if num_clen == 0:
            return True

        # 步骤1.统计每个顶点入度
        in_degree = [0 for _ in range(numCourses)]
        # 邻接表,使用集和去重
        adj = [set() for _ in range(numCourses)]

        for cur, pre in prerequisites:
            in_degree[cur] += 1
            adj[pre].add(cur)

        # 步骤2.将入度为0的顶点加入队列
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            top = queue.popleft()
            count += 1
            # 步骤3.将当前顶点的所有邻接顶点的入度减1，如果入度为0，则加入队列
            for successor in adj[top]:
                in_degree[successor] -= 1
                if in_degree[successor] == 0:
                    queue.append(successor)

        return count == numCourses
