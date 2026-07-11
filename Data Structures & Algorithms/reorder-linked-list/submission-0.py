# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Idea: Traverse the list forwards and backwards at the same time taking turns
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None #split the list (makes forward traverse easy)

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev:
            temp1, temp2 = head.next, prev.next
            head.next = prev
            prev.next = temp1
            prev = temp2
            head = temp1

        
        

        
