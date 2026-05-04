# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        queue = deque([(root, 1)])
        levels = {}

        print(queue)

        while queue:
            node, h = queue.popleft()

            print(node, h)

            # add to levels dict
            if h not in levels:
                levels[h] = [node.val]
            else:
                levels[h].append(node.val)
            
            # add children to queue
            if node.left:
                queue.append((node.left, h + 1))
            if node.right:
                queue.append((node.right, h + 1))

        ans = []
        for val in levels.values():
            ans.append(val)

        return ans
        

            



