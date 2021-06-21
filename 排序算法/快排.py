# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 20:22
# @Author  : wwzhen

class Sort(object):
    def sort(self, nums):
        return self._sort(nums, 0, len(nums) - 1)

    def _sort(self, nums, left, right):
        pivot_key = self._partition(nums, left, right)
        if left < right:
            self._sort(nums, left, pivot_key - 1)
            self._sort(nums, pivot_key + 1, right)
        return nums

    def _partition(self, nums, left, right):
        pivot = nums[left]
        while left < right:
            # 由于pivot = nums[0] 这里是通过pivot进行交换
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]

        nums[left] = pivot
        return left


if __name__ == '__main__':
    s = Sort()
    print(s.sort([3, 4, 2, 1, 5, 6, 7]))
