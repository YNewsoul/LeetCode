import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 使用哈希表，将每个字符串排序，作为哈希表的键，将字符串作为值
        map = {}
        for s in strs:
            # 遍历字符串数组，将每个字符串排序，作为哈希表的键
            key = "".join(sorted(s))
            if key not in map:
                map[key] = []
            map[key].append(s)
        return list(map.values())


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))
