class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for first in range(n - 2):
            # 排序后若第一个数大于 0，后续不可能凑出 0
            if nums[first] > 0:
                break
            # 去重：跳过重复的首元素
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            target = -nums[first]
            second, third = first + 1, n - 1

            while second < third:
                cur = nums[second] + nums[third]
                if cur < target:
                    second += 1
                elif cur > target:
                    third -= 1
                else:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    # 去重：跳过重复的第二、第三个元素
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums))
