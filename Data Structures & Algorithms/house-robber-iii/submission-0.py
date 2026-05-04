# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node.left and not node.right:
                return [node.val, 0]

            # do post-order traversal
            leftSubtree = [0, 0]
            rightSubtree = [0, 0]
            
            if node.left:
                leftSubtree = dfs(node.left)
            
            if node.right:
                rightSubtree = dfs(node.right)

            withRoot = node.val + leftSubtree[1] + rightSubtree[1]
            withoutRoot = max(leftSubtree) + max(rightSubtree)

            return [withRoot, withoutRoot]
    

        return max(dfs(root))

