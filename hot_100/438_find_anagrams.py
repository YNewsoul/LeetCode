from typing import List


# 1.暴力超时解法
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        res = []
        p = sorted(p)
        for i in range(len_s - len_p + 1):
            str = s[i : i + len_p]
            if sorted(str) == p:
                res.append(i)
        return res


# 2.滑动窗口
# 统计滑动窗口和字符串 p 中每种字母数量的差；并引入变量 differ 来记录当前窗口与字符串 p 中数量不同的字母的个数，并在滑动窗口的过程中维护它。
solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))
