# -- coding: utf-8 --
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr) - 2):
            if arr[i] & 2 == arr[i + 1] % 2 == arr[i + 2] % 2 == 1:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    result = solution.threeConsecutiveOdds([2,3,4])
    print result
