# -- coding: utf-8 --
class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        w_list = list()
        n_list = list()
        result = ''
        for x in s:
            try:
                n_list.append(int(x))
            except:
                w_list.append(x)
        if len(n_list) - len(w_list) > 1 or len(n_list) - len(w_list) < -1:
            return result
        if len(n_list) > len(w_list):
            for i in range(len(w_list)):
                result += str(n_list[i]) + w_list[i]
            result += str(n_list[-1])
        elif len(n_list) < len(w_list):
            for i in range(len(n_list)):
                result += w_list[i] + str(n_list[i])
            result += w_list[-1]
        else:
            for i in range(len(n_list)):
                result += w_list[i] + str(n_list[i])
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.reformat("ab123")
    print result
