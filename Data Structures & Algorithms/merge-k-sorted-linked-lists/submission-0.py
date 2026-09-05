# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
given an array of k linked lists, each list is sorted

return the single sorted merged linked list

brute force:
- look at all the smallest elements in the list, take the smallest one and set that as the first, detatch from current list
- repeat until list is empty

instead:
mergesort
    - instead of having to do N * k rounds, can instead merge 2 lists at a time
        - log(k) instead -> O(nlogk)
    


'''

from collections import deque

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        def merge(l1, l2):
            dummy = ListNode(0)
            cur = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            
            cur.next = l1 if l1 else l2
            return dummy.next

        
        q = deque(lists)


        while len(q) > 1:
            l1 = q.popleft()
            l2 = q.popleft()

            q.append(merge(l1, l2))
        
        
        return q[0]
        
