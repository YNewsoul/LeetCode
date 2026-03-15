from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # res[i] 表示 s[:i] 是否可以被 wordDict 中的单词表示
        res = [True]
        for i in range(1, len(s) + 1):
            mark = False
            for j in range(i):
                if res[j] and s[j:i] in wordDict:
                    res.append(True)
                    mark = True
                    break
            if not mark:
                res.append(False)
        return res[-1]


solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))
print(solution.wordBreak("applepenapple", ["apple", "pen"]))
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
