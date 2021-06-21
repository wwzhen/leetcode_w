# -*- coding: utf-8 -*-
# @Time    : 2021/6/17 14:35
# @Author  : wwzhen

class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) < 2:
            return 1
        max_count = 0
        status = s[0]
        cur = 0
        for i in range(0, len(s)):
            if s[i] == status:
                cur += 1
            else:
                status = s[i]
                cur = 1
            max_count = max(cur, max_count)
        return max_count


if __name__ == '__main__':
    s = Solution()
    print(s.maxPower("abbcccddddeeeeedcba"))
