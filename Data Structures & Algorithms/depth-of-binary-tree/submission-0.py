# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root == None: return 0

            stack = collections.deque()
            stack.append((root, 1))

            height = 0

            while stack:
                print(list(stack))
                
                curr = stack.pop()
                
                print(curr[1])

                # if curr[1] > height:
                #     height = curr[1]

                height = max(height, curr[1])

                if curr[0].left: 
                    stack.append((curr[0].left, curr[1] + 1))
                if curr[0].right: 
                    stack.append((curr[0].right, curr[1] + 1))

            return height

        return dfs(root)

            