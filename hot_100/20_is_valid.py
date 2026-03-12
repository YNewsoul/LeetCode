class Solution:
    def isValid(self, s: str) -> bool:
        # 思路：遇到‘)'、']'考虑匹配，s除去匹配的括号
        i = 0
        dic = {")": "(", "]": "[", "}": "{"}
        while i < len(s):
            if s[i] in dic:
                if i > 0 and s[i - 1] == dic[s[i]]:
                    # 去除括号
                    s = s[: i - 1] + s[i + 1 :]
                    # 后退两格
                    i -= 2
                else:
                    return False
            i += 1
        return s == ""
