# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 10:00
# @Author  : wwzhen

# 时间复杂度: O(n), 空间复杂度: O(1)

def sequence_search(nums, target):
    for i in nums:
        if nums[i] == target:
            return nums[target]
    return None

