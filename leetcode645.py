# -- coding: utf-8 --
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        repeat_num = 0
        for i in nums:
            if nums.count(i) > 1:
                repeat_num = i
                break
        t = abs(abs(sum(nums) - sum(range(1, len(nums) + 1))))
        return [repeat_num, repeat_num + t]


if __name__ == '__main__':
    s = Solution()
    print s.findErrorNums([1, 2,2,4])
