# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force solution -> O(n logn)
        k = len(lists)
        
        heap = []


        indices = [None] * k


        for i, l in enumerate(lists):
            heapq.heappush(heap, (l.val, i))
            indices[i] = l.next

        curr = ListNode(0, None)
        head = curr
        while heap:
            curr_min, index = heapq.heappop(heap)
            print(curr_min, index)

            curr.next = ListNode(curr_min, None)
            curr = curr.next

            # repopulate heap
            new_element_in_heap = indices[index]
            if new_element_in_heap != None:
                heapq.heappush(heap, (new_element_in_heap.val, index))
                # actually increment the indices array
                indices[index] = new_element_in_heap.next
        
            print(heap)
        
        return head.next


