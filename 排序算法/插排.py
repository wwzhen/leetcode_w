# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 20:40
# @Author  : wwzhen

class Sort(object):
    def sort(self, nums):
        for i in range(1, len(nums)):
            pre_index = i - 1
            current = nums[i]
            while pre_index >= 0 and nums[pre_index] > current:
                nums[pre_index + 1] = nums[pre_index]
                pre_index -= 1
            nums[pre_index + 1] = current
        return nums


if __name__ == '__main__':
    s = Sort()
    print(s.sort([1, 4, 5, 2, 5]))
