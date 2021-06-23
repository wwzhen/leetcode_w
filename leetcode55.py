# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 17:40
# @Author  : wwzhen
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i in range(len(nums)):
            if max_index >= i and nums[i] + i > max_index:
                max_index = nums[i] + i
            if max_index >= len(nums) - 1:
                return True
        return False
