# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 10:03
# @Author  : wwzhen

# 最好时间复杂度 O(1) 最坏时间复杂度 O(log2n) 平均复杂度 O(log2n)

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        binary = (right + left) // 2
        if target == nums[binary]:
            return nums[binary]
        elif target > nums[binary]:
            left = binary + 1
        else:
            right = binary - 1
    return None
