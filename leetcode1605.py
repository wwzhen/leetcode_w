# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 18:14
# @Author  : wwzhen

# 给你两个非负整数数组rowSum 和colSum，其中rowSum[i]是二维矩阵中第 i行元素的和
# colSum[j]是第 j列元素的和。换言之你不知道矩阵里的每个元素，但是你知道每一行和每一列的和。
# 请找到大小为rowSum.length x colSum.length的任意 非负整数矩阵，且该矩阵满足rowSum 和colSum的要求。
# 请你返回任意一个满足题目要求的二维矩阵，题目保证存在 至少一个可行矩阵。
# https://leetcode-cn.com/problems/find-valid-matrix-given-row-and-column-sums/
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row_len = len(rowSum)
        col_len = len(colSum)
        result = [[0] * col_len for i in range(row_len)]
        for i in range(row_len):
            for j in range(col_len):
                num = min(rowSum[i], colSum[j])
                result[i][j] = num
                rowSum[i] -= num
                colSum[j] -= num
                if rowSum[i] == 0:
                    break
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.restoreMatrix([3, 8], [4, 7]))
