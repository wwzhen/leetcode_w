# -- coding: utf-8 --
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def deep(root):
            if not root:
                return 0
            else:
                return 1 + max(deep(root.left), deep(root.right))

        return deep(root)

