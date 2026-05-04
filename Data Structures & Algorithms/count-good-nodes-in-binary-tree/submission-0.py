# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # run dfs with another stack containing the curr_max

        stack = []
        max_stack = []
        good = 0

        stack.append(root)
        max_stack.append(root.val)

        while stack:
            node = stack.pop()
            node_val = node.val
            curr_max = max_stack.pop()

            r = node.right
            l = node.left

            if r:
                stack.append(r)
                max_stack.append(max(curr_max, r.val))
            if l: 
                stack.append(l)
                max_stack.append(max(curr_max, l.val))
            
            if node_val >= curr_max:
                good += 1
        
        return good


