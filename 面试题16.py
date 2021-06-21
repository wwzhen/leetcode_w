# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 19:53
# @Author  : wwzhen

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        op_index = list()
        for i,c in enumerate(s):
            if c in "*/":
                op_index.append(i)
                import re
                re.sub()
