# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 22:03
# @Author  : wwzhen
from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        types = dict()
        temp_types = dict()
        i, j = 0, 0
        count = 0
        while i < len(tree):
            if len(types) == 2 and types.get(tree[i], None) is None:
                types = temp_types.copy()
            else:
                types[tree[i]] = types.get(tree[i], 0) + 1
                temp_types[tree[i]] = temp_types.get(tree[i], 0) + 1
                if tree[i] != tree[j]:
                    del temp_types[tree[j]]
                j = i
                i += 1
            count = max(count, sum(types.values()))
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.totalFruit([0, 1, 6, 6, 4, 4, 6]))
