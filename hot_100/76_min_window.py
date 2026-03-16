class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid(hash_map, hash_map_t):
            if len(hash_map) < len(hash_map_t):
                return False
            for char in hash_map_t:
                if hash_map.get(char, 0) < hash_map_t[char]:
                    return False
            return True

        len_s, len_t = len(s), len(t)
        hash_map = {}
        hash_map_t = {}
        for char in t:
            hash_map_t[char] = hash_map_t.get(char, 0) + 1
        min_len = len_s
        left, min_left, min_right = 0, 0, len_s - 1
        find = False
        for i in range(len_s):
            if s[i] in t:
                hash_map[s[i]] = hash_map.get(s[i], 0) + 1
                # 已找到包含t所有字符的子串
                if is_valid(hash_map, hash_map_t):
                    find = True
                    # 把left指针移动到t中字符的位置
                    while True:
                        if s[left] not in t:
                            left += 1
                            continue
                        if hash_map[s[left]] > hash_map_t[s[left]]:
                            hash_map[s[left]] -= 1
                            left += 1
                            continue
                        break
                    if i - left + 1 < min_len:
                        min_len = i - left + 1
                        min_left = left
                        min_right = i
        return s[min_left : min_right + 1] if find else ""


solution = Solution()
# print(solution.minWindow("ADOBECODEBANC", "ABC"))
print(solution.minWindow("aa", "aa"))
# print(solution.minWindow("a", "aa"))
