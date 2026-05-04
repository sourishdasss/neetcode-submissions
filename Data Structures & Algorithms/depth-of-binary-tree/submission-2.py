# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        # start dfs
        h = 0
        stack = [[root, 1]]

        while stack:
            node, tmp_h = stack.pop()
            h = max(h, tmp_h)
            if node.left:
                stack.append([node.left, tmp_h + 1])
            if node.right:
                stack.append([node.right, tmp_h + 1])

        return h
