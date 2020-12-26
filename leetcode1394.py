# -- coding: utf-8 --

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky_num = -1
        for i in arr:
            if lucky_num < i == arr.count(i):
                lucky_num = i
        return lucky_num


if __name__ == '__main__':
    s = Solution()
    print s.findLucky([2, 2, 3, 4])
