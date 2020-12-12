# -- coding: utf-8 --

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        nb = text.count('b')
        na = text.count('a')
        nl = text.count('l') / 2
        no = text.count('o') / 2
        nn = text.count('n')
        return min(nb, na, nl, no, nn)


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxNumberOfBalloons("nlaebolko")
    print result
