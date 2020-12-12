# -- coding: utf-8 --

class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        count = 0 if int(target[0]) == 0 else 1
        for i in range(len(target) - 1):
            if target[i] != target[i + 1]:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    result = s.minFlips("001011101")
    print result
