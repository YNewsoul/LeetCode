"""
输入输出控制
"""

import sys

# 1.读取一个整数
# n = int(input())
# print(n)

# 2.读取一个字符串
# s = input().strip() # 移除首尾空格/换行符
# print(s)

# 3.读取一行
# nums = list(map(int,input().split()))
# print(nums[0],nums[1])
# print(s)

# 4.未知行数，读到文件结束（EOF）
# while line := sys.stdin.readline():
#     print(line)

# 5.输出
nums = [1, 2, 3]
print(
    " ".join(map(str, nums))
)  # map(str, nums):把列表里每个数字转为字符串，得到 ["1","2","3"]
# ' '.join(map(str, nums))):把列表里的每个字符串用空格连接起来，得到 "1 2 3"
