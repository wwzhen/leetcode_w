# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 17:41
# @Author  : wwzhen


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False
        i, j = 0, 0
        n = len(start)
        while i < n or j < n:
            while j < n and end[j] == 'X':
                j += 1
            while i < n and start[i] == 'X':
                i += 1
            if i < n ^ j < n:
                return False
            if i < n and j < n:
                if start[i] != end[j] or (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                    return False
            i += 1
            j += 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canTransform("XRXXXLXXXR", "XXRLXXXRXX"))
