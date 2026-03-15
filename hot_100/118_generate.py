from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 定义 res[i] 为第 i 行的元素列表
        res = []
        res.append([1])
        for i in range(1, numRows):
            # 定义 cur 为第 i 行的元素列表
            cur = []
            cur.append(1)
            for j in range(1, i):
                cur.append(res[i - 1][j - 1] + res[i - 1][j])
            cur.append(1)
            res.append(cur)
        return res


solution = Solution()
print(solution.generate(5))
print(solution.generate(1))
