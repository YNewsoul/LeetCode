import collections
from typing import List


class Solution:
    # 思路：构建一个存储列表的集合
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in map:
                map[key] = []
            map[key].append(s)
        return list(map.values())


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))
