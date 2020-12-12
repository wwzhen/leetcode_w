# -- coding: utf-8 --

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print s.findNumbers([123,22,2,1232,1])