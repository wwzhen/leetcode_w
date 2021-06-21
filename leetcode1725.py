# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 21:28
# @Author  : wwzhen
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = 0
        max_len = 0  # 最长的正方形边长

        for i in rectangles:
            cur_square_len = min(i[0], i[1])  # 当前矩形可以切出的最大正方形的边长
            if cur_square_len > max_len:  # 如果更大。重新统计
                max_len = cur_square_len
                cnt = 1
                continue
            elif cur_square_len == max_len:
                cnt += 1
        return cnt
