def zero_one_knapsack(weights, values, capacity):
    """
    01背包问题
    """
    n = len(weights)
    # dp[i][j] = 前 i 个物品，背包容量 j 时的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # 当前物品装不下
            if j < weights[i - 1]:
                dp[i][j] = dp[i - 1][j]
            # 可以装：选 不装 / 装 中价值更大的
            else:
                dp[i][j] = max(
                    dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1]
                )
    return dp[n][capacity]


def unbounded_knapsack_2d(weights, values, capacity):
    n = len(weights)
    # dp[i][j]：前i个物品，容量j的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if j < weights[i - 1]:
                # 装不下，沿用前i-1件结果
                dp[i][j] = dp[i - 1][j]
            else:
                # 不选当前品 / 选当前品(可重复选)取最大值
                # 选当前品(可重复选)：dp[i][j-weights[i-1]]
                # 不选当前品：dp[i-1][j]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]


def multiple_knapsack_2d(weights, values, counts, capacity):
    n = len(weights)
    # dp[i][j] = 前 i 种物品，背包容量 j 时的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # 尝试放 0 ~ cnt 个当前物品，取价值最大的一种
            max_val = 0
            # k 是放的个数：0,1,2,...,最多cnt个，且不超重
            for k in range(0, min(counts[i - 1], j // weights[i - 1]) + 1):
                max_val = max(
                    max_val, dp[i - 1][j - k * weights[i - 1]] + k * values[i - 1]
                )
            dp[i][j] = max_val
    return dp[n][capacity]


# 测试
if __name__ == "__main__":
    w = [2, 3, 4, 5]  # 物品重量
    v = [3, 4, 5, 6]  # 物品价值
    c = 8  # 背包容量
    print("01背包最大价值:", zero_one_knapsack(w, v, c))  # 输出 10
    print("完全背包最大价值:", unbounded_knapsack_2d(w, v, c))  # 输出 12
