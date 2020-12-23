# -- coding: utf-8 --
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # if len(word) == 1:
        #     return True
        # else:
        #     if word.upper() == word or word.lower() == word:
        #         return True
        #     elif word[1:].lower() == word[1:]:
        #         return True
        #     else:
        #         return False
        return word.upper() == word or word.lower() == word or word.title() == word



if __name__ == '__main__':
    s = Solution()
    print s.detectCapitalUse("USA")
