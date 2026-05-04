# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []


        q = deque([])
        q.append(root)

        print(q)

        ans = []
        stack = []
        tmp = []
        level = 0
        while q:
            curr = q.popleft()
            tmp.append(curr.val)

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

            # check if we finished traversing level
            if not q:
                if level % 2 == 0:
                    ans.append(tmp)
                else:
                    ans.append(reversed(tmp))

                for t in stack:
                    q.append(t)
                tmp = []
                stack = []
                level += 1
        
        return ans
        

            