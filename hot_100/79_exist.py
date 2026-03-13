from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def reasonable(path, visited, i, j):
            if not (
                0 <= i < len(board) and 0 <= j < len(board[0]) and not visited[i][j]
            ):
                return False
            path.append(board[i][j])
            visited[i][j] = True
            if backtrack(visited, path, i, j):
                return True
            path.pop()
            visited[i][j] = False

        def backtrack(visited, path, i, j):
            # 易错点3: 每次递归时, 要判断当前位置是否与单词中的字符匹配，不匹配则返回 False.
            if path[-1] != word[len(path) - 1]:
                return False

            if "".join(path) == word:
                return True

            # 上下左右
            if reasonable(path, visited, i - 1, j):
                return True
            if reasonable(path, visited, i + 1, j):
                return True
            if reasonable(path, visited, i, j - 1):
                return True
            if reasonable(path, visited, i, j + 1):
                return True

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 易错点1: 回溯时, 要将当前位置加入路径, 并将当前位置标记为已访问.
                visited[i][j] = True
                if backtrack(visited, [board[i][j]], i, j):
                    return True
                # 易错点2: 回溯时, 要将当前位置从路径中移除, 并将当前位置标记为未访问.
                visited[i][j] = False
        return False


solution = Solution()
print(
    solution.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
)
print(
    solution.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
    )
)
print(
    solution.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
    )
)
print(solution.exist([["a"]], "a"))
print(solution.exist([["a", "a"]], "aaa"))
print(solution.exist([["a", "b"]], "ba"))
print(
    solution.exist(
        [
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "B"],
            ["A", "A", "A", "A", "B", "A"],
        ],
        "BBAAAAAAAAAAAAA",
    )
)
