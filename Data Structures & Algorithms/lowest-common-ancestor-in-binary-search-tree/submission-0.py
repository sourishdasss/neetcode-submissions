# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        p_val = p.val
        q_val = q.val

        while True:
            curr_val = curr.val
            if p_val < curr_val and q_val < curr_val:
                curr = curr.left
            elif p_val > curr_val and q_val > curr_val:
                curr = curr.right
            else:
                return curr
                
