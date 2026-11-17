"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {None: None}
        current = head

        while current is not None:
            seen[current] = Node(current.val)
            current = current.next

        current = head

        while current is not None:
            duplicate = seen[current]
            duplicate.next = seen[current.next]
            duplicate.random = seen[current.random]
            current = current.next

        return seen[head]