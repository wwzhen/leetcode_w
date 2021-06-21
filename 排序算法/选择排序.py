# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 19:44
# @Author  : wwzhen
from typing import List


class Sort(object):
    def sort(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            min_num = min(nums)
            result.append(min_num)
            del nums[nums.index(min_num)]
        return result


if __name__ == '__main__':
    s = Sort()
    print(s.sort([4, 2, 3, 2, 1, 1, 1, 5]))
