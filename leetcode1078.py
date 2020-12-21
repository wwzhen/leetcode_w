# -- coding: utf-8 --

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text_list = text.split(' ')
        result = list()
        for i in range(len(text_list) - 2):
            if text_list[i] == first and text_list[i + 1] == second:
                result.append(text_list[i + 2])
        return result


if __name__ == '__main__':
    s = Solution()
    print s.findOcurrences("we will we will rock you", "we", "will")
