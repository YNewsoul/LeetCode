from typing import List


# 560.和为 K 的子数组
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和出现次数：prefix_count[s] 表示前缀和 s 出现的次数
        prefix_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            # 若存在 prefix_sum - k，则说明有若干子数组和为 k
            count += prefix_count.get(prefix_sum - k, 0)
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))
    print(solution.subarraySum([1, 2, 3], 3))
    print(solution.subarraySum([1, -1, 0], 0))
