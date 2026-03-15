class Solution:
    def climbStairs(self, n: int) -> int:
        # 定义 need[i] 为到达第 i 级台阶的不同方法数
        # need[0] = need[1] = 1
        need = []
        need.append(1)
        need.append(1)
        for i in range(2, n + 1):
            need.append(need[i - 1] + need[i - 2])
        return need[n]


solution = Solution()
print(solution.climbStairs(2))
print(solution.climbStairs(3))
