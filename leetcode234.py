# -- coding: utf-8 --
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        p_list = list()
        while p:
            p_list.append(p.val)
            p = p.next
        if p_list == p_list.reverse():
            return True
        else:
            return False

