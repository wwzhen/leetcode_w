# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 19:44
# @Author  : wwzhen
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

    def missingNumber2(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([0, 1, 2, 3, 5]))
