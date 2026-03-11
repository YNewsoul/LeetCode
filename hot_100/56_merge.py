from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先按照区间起始位置排序
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i][0] = intervals[i - 1][0]
                intervals[i][1] = max(intervals[i - 1][1], intervals[i][1])
            else:
                res.append(intervals[i - 1])
        res.append(intervals[-1])
        return res


solution = Solution()
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solution.merge([[1, 4], [4, 5]]))
print(solution.merge([[4, 7], [1, 4]]))
