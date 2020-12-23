# -- coding: utf-8 --
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_dict = dict()
        for i in nums:
            num_dict[i] = nums.count(i)
        sorted_nums = sorted(nums, key=lambda x: (num_dict[x], x))
        return sorted_nums

if __name__ == '__main__':
    s = Solution()
    print s.frequencySort([1,1,2,2,2,3])