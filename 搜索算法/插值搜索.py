# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 10:29
# @Author  : wwzhen

# 时间复杂度 O(loglogn)

def insert_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        midpoint = left + (target - nums[left]) // (nums[right] - nums[left]) * (right - left)
        if nums[midpoint] == target:
            return midpoint
        elif target > nums[midpoint]:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return None
