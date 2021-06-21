# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 12:07
# @Author  : wwzhen

class Sort(object):
    def sort(self, nums):
        return self._sort(nums)

    def _sort(self, nums):
        if len(nums) < 2:
            return nums
        middle_place = len(nums) // 2
        left = nums[0: middle_place]
        right = nums[middle_place:]
        return self._merge(self._sort(left), self._sort(right))

    def _merge(self, left, right):
        result = list()
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left[0])
                del left[0]
            else:
                result.append(right[0])
                del right[0]
        while len(left):
            result.append(left[0])
            del left[0]
        while len(right):
            result.append(right[0])
            del right[0]
        return result


if __name__ == '__main__':
    s = Sort()
    print(s.sort([6, 5, 4, 3, 2, 1, 9]))
