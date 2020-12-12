# -- coding: utf-8 --

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        t5 = 0
        t10 = 0
        for bill in bills:
            if bill == 5:
                t5 += 1
            elif bill == 10:
                if t5:
                    t5 -= 1
                    t10 += 1
                else:
                    return False
            elif bill == 20:
                if not t5:
                    return False
                elif t10:
                    t10 -= 1
                    t5 -= 1
                elif t5 >= 3:
                    t5 -= 3
                else:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.lemonadeChange([5, 5, 10, 10, 20])
    print result
