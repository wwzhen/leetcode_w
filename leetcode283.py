# -- coding: utf-8 --
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in nums:
            if i != 0:
                nums[j] = i
                j += 1
        for k in range(j, len(nums)):
            nums[k] = 0
        return nums


if __name__ == '__main__':
    s = Solution()
    print s.moveZeroes([0,0,1])
