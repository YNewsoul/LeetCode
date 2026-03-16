from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        len_nums = len(nums)
        k_queue = deque()
        for i in range(k):
            while k_queue and nums[i] >= nums[k_queue[-1]]:
                k_queue.pop()
            k_queue.append(i)
        ans = [nums[k_queue[0]]]
        for i in range(k, len_nums):
            while k_queue and nums[i] >= nums[k_queue[-1]]:
                k_queue.pop()
            k_queue.append(i)
            while k_queue[0] <= i - k:
                k_queue.popleft()
            ans.append(nums[k_queue[0]])
        return ans
