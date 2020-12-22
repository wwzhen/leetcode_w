# -- coding: utf-8 --
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res_str = ""
        words = sorted(words, key=lambda x: len(x), reverse=True)
        for i in range(len(words)):
            is_have = False
            for j in range(i):
                if words[i] in words[j] and words[i] == words[j][-len(words[i]):]:
                    is_have = True
                    break
            if not is_have:
                res_str += words[i] + "#"
        return len(res_str)


if __name__ == '__main__':
    s = Solution()
    print s.minimumLengthEncoding(["me", "time"])
