# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 22:48
# @Author  : wwzhen
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        index = len(students) - 1
        while i <= index:
            if (sandwiches[i] == 1 and 1 not in students) or (sandwiches[i] == 0 and 0 not in students):
                return len(students)
            if students[i] == sandwiches[i]:
                del sandwiches[i]
            else:
                students.append(students[i])
            del students[i]
            index -= 1
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.countStudents([0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
                          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0]))
