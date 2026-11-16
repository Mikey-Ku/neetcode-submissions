# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current != None:
            length += 1
            current = current.next

        if n == length:
            return head.next
            
        search = head
        head = search
        i = 0
        while i < (length - n) - 1:
            search = search.next
            i += 1
        
        search.next = search.next.next

        return head

