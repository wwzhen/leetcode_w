# -- coding: utf-8 --
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0
        j = k
        k_sum = sum(nums[i:k])
        while j < len(nums):
            j += 1
            i += 1
            n_sum = sum(nums[i:j])
            k_sum = n_sum if n_sum > k_sum else k_sum
        return k_sum / float(k)


if __name__ == '__main__':
    s = Solution()
    print s.findMaxAverage([0, 1, 1, 3, 3], 4)
