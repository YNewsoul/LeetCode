from typing import List

# 128.最长连续序列
"思路：哈希表，集合去重"


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 将数组转换为集合去重
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            # 如果当前数字的前一个数字不在集合中，说明当前数字是连续序列的开始
            if num - 1 not in nums_set:
                cur_num = num
                cur_len = 1
                # 遍历当前数字的后一个数字，直到后一个数字不在集合中
                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_len += 1
                max_len = max(max_len, cur_len) if max_len else cur_len
        return max_len


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
