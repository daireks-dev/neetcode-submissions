# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        head2 = head
        
        while head2 and head2.next:
            head = head.next

            if head2.next:
                head2 = head2.next.next
            else:
                head2 = head2.next

            if head == head2:
                return True

        return False
        
                

