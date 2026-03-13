# 各种排序算法


from typing import List


class SortingAlgorithm:
    def insertion_sort(self, nums: List[int] = [5, 2, 3, 4, 7, 1]) -> List[int]:
        # 1.插入排序,将数组分为已排序和未排序两部分,每次从未排序部分取一个元素插入到已排序部分的合适位置
        # 时间复杂度O(n^2),空间复杂度O(1),稳定排序
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                # 关键点，将大于key的元素后移一位
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums

    def bubble_sort(self, nums: List[int] = [5, 2, 3, 4, 7, 1]) -> List[int]:
        # 2.冒泡排序
        # 时间复杂度O(n^2),空间复杂度O(1),稳定排序
        for i in range(len(nums)):
            # 添加一个标志位，用于判断是否有交换操作，可提前结束
            swapped = False
            # 内层控制轮数,-1-i表示已经有i+1个元素有序
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    # 前者大于后者，将大的往后挪
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums

    def selection_sort(self, nums: List[int] = [5, 2, 3, 4, 7, 1]) -> List[int]:
        # 3.选择排序,可同时找到最大和最小元素,将其放到数组的两端
        # 时间复杂度O(n^2),空间复杂度O(1),不稳定排序
        left = 0
        right = len(nums) - 1
        while left < right:
            min_index = left
            max_index = right
            for i in range(left, right + 1):
                if nums[i] < nums[min_index]:
                    min_index = i
                if nums[i] > nums[max_index]:
                    max_index = i
            if min_index != left:
                nums[left], nums[min_index] = nums[min_index], nums[left]
            # 最小值交换了，最大值可能也交换了，所以要更新最大值的索引
            if max_index == left:
                max_index = min_index
            if max_index != right:
                nums[right], nums[max_index] = nums[max_index], nums[right]
            left += 1
            right -= 1
        return nums

    def quick_sort(self, nums: List[int] = [5, 2, 3, 4, 7, 1]) -> List[int]:
        # 4.快速排序,通过分治法将数组分为两部分,分别对其排序
        # 时间复杂度O(nlogn),空间复杂度O(logn),不稳定排序
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def merge_sort(self, nums: List[int] = [5, 2, 3, 4, 7, 1]) -> List[int]:
        # 5.归并排序（主函数：负责拆分）
        # 时间复杂度O(nlogn),空间复杂度O(n),稳定排序

        # 合并函数：把两个有序数组合成一个有序数组
        def _merge(left, right):
            result = []
            i = j = 0  # 两个指针，分别遍历 left 和 right

            # 5.3 谁小就先拿谁
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # 5.4 把剩下的元素直接加进去
            result += left[i:]
            result += right[j:]

            return result

        # 递归终止条件：只剩1个元素，不用排
        if len(nums) <= 1:
            return nums

        # 5.1 从中间拆分
        mid = len(nums) // 2
        # 递归拆分左边
        left = self.merge_sort(nums[:mid])
        # 递归拆分右边
        right = self.merge_sort(nums[mid:])

        # 5.2. 合并两个有序数组
        return _merge(left, right)


sorting = SortingAlgorithm()
print(sorting.insertion_sort())
print(sorting.bubble_sort())
print(sorting.selection_sort())
print(sorting.quick_sort())
print(sorting.merge_sort())
