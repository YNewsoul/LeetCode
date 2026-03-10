from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur_num = num
                cur_len = 1
                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_len += 1
                max_len = max(max_len, cur_len) if max_len else cur_len
        return max_len


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
