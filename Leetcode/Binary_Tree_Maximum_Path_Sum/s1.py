# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        res = -987654321

        def seq(node):
            nonlocal res
            if node is None:
                return 0
            left = max(0, seq(node.left))
            right = max(0, seq(node.right))
            res = max(res, node.val + left + right)
            return node.val + max(left, right)

        seq(root)
        return res



