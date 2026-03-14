from typing import List

# 287. 寻找重复数
# 思路：因为在区间 [1,n] 内存在重复的数。我们先累计大小在 [1,⌊n/2⌋] 之间的数字个数
# 如果重复数在这个范围内，则个数 >⌊n/2n⌋,否则可确定区间 [⌊n/2n⌋,n]  内存在重复数。即可通过二分查找求解


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        min_val = 1  # 所查找数字范围的最小值
        max_val = len(nums)  # 所查找数字范围的最大值

        while min_val < max_val:
            mid = (min_val + max_val) // 2
            # 计数
            cnt = sum(min_val <= num <= mid for num in nums)

            if cnt > mid - min_val + 1:  # 个数超出范围长度，即存在重复数
                max_val = mid
            else:
                min_val = mid + 1

        return min_val
