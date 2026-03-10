# 3. 无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 1 if len(s) != 0 else 0
        start = 0
        for i in range(1, len(s)):
            if s[i] in s[start:i]:
                start = s.index(s[i], start, i) + 1
                max_len = max(max_len, i - start + 1)
            else:
                max_len = max(max_len, i - start + 1)
        return max_len


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))
