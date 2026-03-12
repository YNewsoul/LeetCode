class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            # 从末尾开始
            if char == "]":
                cur = ""
                while stack and stack[-1] != "[":
                    cur = stack.pop() + cur
                stack.pop()  # 弹出'['
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(cur * int(num))
            else:
                stack.append(char)
        return "".join(stack)


solution = Solution()
# print(solution.decodeString("3[a]"))
print(solution.decodeString("100[leetcode]"))
# print(solution.decodeString("3[2[c]]"))
# print(solution.decodeString("2[abc]3[cd]ef"))
