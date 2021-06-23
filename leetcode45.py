# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 18:47
# @Author  : wwzhen
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_i = 0
        step = 0
        end = 0
        n = len(nums) - 1
        for i in range(len(nums) - 1):
            max_i = max(max_i, nums[i] + i)
            if i == end:
                end = max_i
                step += 1
        return step
