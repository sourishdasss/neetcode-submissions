# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(p, q):
            queue_p = collections.deque()
            queue_p.append(p)
            queue_q = collections.deque()
            queue_q.append(q)
            
            while queue_p or queue_q:
                curr_p = None
                curr_q = None
                
                # Check for different tree structure
                if queue_p and queue_q:
                    curr_p = queue_p.popleft()
                    curr_q = queue_q.popleft()
                elif queue_p:
                    return False
                elif queue_q:
                    return False

                # Check for same value
                if curr_p and curr_q:
                    if curr_p.val != curr_q.val:
                        return False
                elif curr_p:
                    return False
                elif curr_q:
                    return False
                
                if curr_p:
                    queue_p.append(curr_p.left)
                    queue_p.append(curr_p.right)
                if curr_q:
                    queue_q.append(curr_q.left)
                    queue_q.append(curr_q.right)

            return True

        return bfs(p, q)

