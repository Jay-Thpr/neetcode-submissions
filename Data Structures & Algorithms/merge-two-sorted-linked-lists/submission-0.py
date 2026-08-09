# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        latest = head
        while l1 and l2:
            if l1.val < l2.val:
                latest.next = l1
                latest = latest.next
                l1 = l1.next
            else:
                latest.next = l2
                latest = latest.next
                l2 = l2.next
        
        if l1:
            latest.next = l1
        else:
            latest.next = l2
        
        return head
            
                
            

        