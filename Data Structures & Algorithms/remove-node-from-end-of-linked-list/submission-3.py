# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        target = length - n
        index = 0
        prev = None
        current = head
        while current:
            if index == target:
                if index == 0:
                    head = head.next
                elif index == length - 1:
                    prev.next = None
                    current = None
                else:
                    temp = current.next
                    current = None
                    prev.next = temp
                break

            index += 1
            prev = current
            current = current.next

        return head
