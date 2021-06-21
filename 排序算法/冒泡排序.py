# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 19:35
# @Author  : wwzhen
from typing import List


class Sort(object):
    def sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

if __name__ == '__main__':
    s = Sort()
    print(s.sort([2,3,4,1,3]))