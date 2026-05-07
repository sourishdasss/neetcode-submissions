# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node):
            # check if leaf node
            if not node.left and not node.right:
                return 1
            
            # run dfs on children
            leftTree, rightTree = 0, 0
            if node.left:
                leftTree = dfs(node.left)
            if node.right:
                rightTree = dfs(node.right)

            tmp_max = leftTree + rightTree
            self.max_diameter = max(self.max_diameter, tmp_max)
            
            return 1 + max(leftTree, rightTree)

        dfs(root)
        return self.max_diameter


            
