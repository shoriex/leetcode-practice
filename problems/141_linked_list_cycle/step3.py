# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# input:
# ListNode(val=3, next=(pointer_2))
# -> ListNode(val=2, next=(pointer_0)),
# -> ListNode(val=0, next=(pointer_-4))
# -> ListNode(val=-4, next=(pointer_2))

# output: true
from typing import Optional


class Solution:

    def hasCycle1(self, head: Optional["ListNode"]) -> bool:
        visited_nodes = set()

        node = head
        while node is not None:
            if node in visited_nodes:
                return True
            visited_nodes.add(node)
            node = node.next

        return False

    def hasCycle2(self, head: Optional["ListNode"]) -> bool:
        fast_pointer = head
        if head is None:
            return False
        second_pointer = head.next

        while second_pointer is not None:
            if fast_pointer is second_pointer:
                return True
            fast_pointer = fast_pointer.next
            
            if second_pointer.next is None:
                break
            second_pointer = second_pointer.next.next

        return False
