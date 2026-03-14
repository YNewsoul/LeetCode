from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 步骤1.统计每个元素出现的次数
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        # 步骤2.将元素出现次数转换为列表
        num_count_list = list(num_count.items())

        # 步骤3.对元素出现次数列表进行排序
        num_count_list.sort(key=lambda x: x[1], reverse=True)

        # 步骤4.返回前k个元素
        return [num_count_list[i][0] for i in range(k)]


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
