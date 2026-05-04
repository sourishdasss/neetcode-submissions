# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        indices = [None] * k

        for i, l in enumerate(lists):
            indices[i] = l

        print(indices)

        heap = []
        # populate heap
        for i in indices:
            while i:
                heapq.heappush(heap, i.val)
                i = i.next

        print(heap)

        curr = None
        front = None
        if heap:
            front = ListNode(heapq.heappop(heap), None)
            curr = front

        print(front, curr)

        while heap:
            tmp = ListNode(heapq.heappop(heap), None)
            print(tmp)
            curr.next = tmp
            curr = tmp
        
        return front
