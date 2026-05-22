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
    def findAnagrams_(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        # 统计s和p中每个字母的数量
        s_count = [0] * 26
        p_count = [0] * 26
        #
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        # 如果s和p中每个字母的数量都相同，说明s的前p_len个字符是p的异位词
        if s_count == p_count:
            ans.append(0)

        # 滑动窗口，更新s_count中的字母数量
        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                ans.append(i + 1)

        return ans


solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))
