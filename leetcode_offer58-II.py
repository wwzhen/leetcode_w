# -- coding: utf-8 --
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        res = s[n:] + s[0:n]
        return res


if __name__ == '__main__':
    s = Solution()
    print s.reverseLeftWords("abcdefg", 2)
