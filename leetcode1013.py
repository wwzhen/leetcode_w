class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_sum = sum(arr)
        if arr_sum % 3:
            return False
        i = 0
        j = len(arr) - 1
        sum_left = arr[i]
        sum_right = arr[j]
        avg = arr_sum / 3
        while i < j - 1:
            if sum_left == sum_right == avg:
                return True
            else:
                if sum_left != avg:
                    i += 1
                    sum_left += arr[i]
                if sum_right != avg:
                    j -= 1
                    sum_right += arr[j]
        return False