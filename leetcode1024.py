# -- coding: utf-8 --

class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        # 按起始时间排序
        clips.sort()



if __name__ == '__main__':
    s = Solution()
    print s.videoStitching(
        [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5],
         [5, 7], [6, 9]], 9)
