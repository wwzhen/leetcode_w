# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 21:13
# @Author  : wwzhen

# 有一个由小写字母组成的字符串 S，和一个整数数组 shifts。
# 我们将字母表中的下一个字母称为原字母的 移位（由于字母表是环绕的， 'z'将会变成'a'）。
# 例如·，shift('a') = 'b'，shift('t') = 'u',， 以及shift('z') = 'a'。
# 对于每个shifts[i] = x， 我们会将 S中的前i+1个字母移位x次。
# 返回将所有这些移位都应用到 S 后最终得到的字符串。
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        x = sum(shifts) % 26
        result = []
        for index, c in enumerate(s):
            result.append(chr(ord('a') + (ord(c) - ord('a') + x) % 26))
            x -= shifts[index]
        return "".join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.shiftingLetters('dab', [10, 20, 30]))
