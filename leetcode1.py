# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 17:37
# @Author  : wwzhen
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, num in enumerate(nums):
            if dic.get(target-num, None) is not None:
                return [i, dic[target-num]]
            else:
                dic[num] = i
