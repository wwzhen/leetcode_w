# -- coding: utf-8 --

class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        # target_list = list(target)
        # init_list = [0] * len(target_list)
        # count = 0
        # for i in range(len(target_list)):
        #     if int(target_list[i]) != init_list[i]:
        #         count += 1
        #         init_list = self.flip(init_list)
        # return count


    def flip(self, l):
        for i in range(len(l)):
            l[i] = 0 if l[i] else 1
        return l


if __name__ == '__main__':
    s = Solution()
    result = s.minFlips("001011101")
    print result
