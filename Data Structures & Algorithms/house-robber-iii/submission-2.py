# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # format: [with_root, without_root]


        def dfs(node):
            # base case
            if not node.left and not node.right:
                return [node.val, 0]

            # run dfs on neighbours
            left_subtree = [0, 0]
            right_subtree = [0, 0]

            if node.left:
                left_subtree = dfs(node.left)

            if node.right:
                right_subtree = dfs(node.right)
            
            with_root = node.val + left_subtree[1] + right_subtree[1]
            without_root = max(left_subtree) + max(right_subtree)

            return [with_root, without_root]
        
        return max(dfs(root))
