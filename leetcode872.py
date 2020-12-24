# -- coding: utf-8 --
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = []
        leaf2 = []

        def search_leaf(node, leaf):
            if not node:
                return
            if not node.left and not node.right:
                leaf.append(node.val)
            else:
                search_leaf(node.left, leaf)
                search_leaf(node.right, leaf)

        search_leaf(root1, leaf1)
        search_leaf(root2, leaf2)
        return leaf1 == leaf2
