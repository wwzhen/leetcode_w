# -- coding: utf-8 --
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = list()
        # 将num的值作为下标，将下标对应的值取反，若取到复数，则说明这个值访问过，下标重复
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(abs(num))
            else:
                nums[index] = -nums[index]
        return res


if __name__ == '__main__':
    s = Solution()
    print s.findDuplicates([6, 4, 5, 2, 1, 1])
