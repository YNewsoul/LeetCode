from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 1.统计每个字符最后出现的位置
        last = {c: i for i, c in enumerate(s)}

        res, start, end = [], 0, 0
        for i in range(len(s)):
            # 2.找到当前字符最后出现的位置
            end = max(end, last[s[i]])
            # 如果到达当前能到达的最远位置的索引，说明当前位置是一个分割点
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res


solution = Solution()
print(solution.partitionLabels("ababcbacadefegdehijhklij"))
print(solution.partitionLabels("eccbbbbdec"))
