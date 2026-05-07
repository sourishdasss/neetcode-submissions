# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node.left and not node.right:
                return tuple((True, 1))

            # run dfs on children
            left_balance, left_height = (True, 0)
            right_balance, right_height = (True, 0)

            if node.left:
                left_balance, left_height = dfs(node.left)
            if node.right:
                right_balance, right_height = dfs(node.right)

            # check for in-balance
            if abs(left_height - right_height) > 1 or not left_balance or not right_balance:   
                return tuple((False, 0))
            else:
                return tuple((True, max(left_height, right_height) + 1))
        
        # check if root exists
        if not root:
            return True

        return dfs(root)[0]