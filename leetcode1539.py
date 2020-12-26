# -- coding: utf-8 --
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i = 1
        while k > 0:
            if i not in arr:
                k -= 1
            i += 1
        return i - 1


if __name__ == '__main__':
    s = Solution()
    print s.findKthPositive([1,2,3,4], 2)
