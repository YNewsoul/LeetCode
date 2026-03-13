from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def letterCombinations(self, digits: str) -> List[str]:
        digit_all = [
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"],
        ]

        def backtrack(path, start):
            if len(path) == len(digits):
                self.res.append(path[:])
                return
            for j in range(len(digit_all[int(digits[start]) - 2])):
                path += digit_all[int(digits[start]) - 2][j]
                backtrack(path, start + 1)
                # 关键点：回溯时，需要将当前节点从路径中删除
                path = path[:start]

        backtrack("", 0)
        return self.res


solution = Solution()
print(solution.letterCombinations("23"))
print(solution.letterCombinations("2"))
