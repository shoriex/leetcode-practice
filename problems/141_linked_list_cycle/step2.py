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

# Memo

# Strategy 1. Traverse all nodes from the head and store them to track 
# visited nodes.
# If a node is revised, the list contains a cycle.
# This approach is easy to implement but requires O(n) space conplexity.

# Strategy 2. Use two pointers moving at diffrent speeds. The first pointer
# moves 1 node per step, while the second pointer moves 2 nodes per step.
# This approach is a bit tricky but archieves O(1) space complexity.

# Example: A -> B -> C -> D -> A
# First Pointer:  A -> B -> C -> D
# Second Pointer: B -> D -> B -> D

from typing import Optional


class Solution:

    # Strategy 1
    def hasCycle1(self, head: Optional["ListNode"]) -> bool:
        visited_node = set()

        while(head is not None):
            # 1. Check      
            if head in visited_node:
                return True
            # 2. Update vistied_node
            visited_node.add(head)
            # 3. Update head
            head = head.next
        
        return False

    # Strategy 2
    def hasCycle(self, head: Optional["ListNode"]) -> bool:
        
        pointer1 = head
        pointer2 = head.next if head is not None else None

        while(pointer2 is not None):
            # 1. Check
            if pointer1 == pointer2:
                return True

            # 2. Update
            pointer1 = pointer1.next
            pointer2 = None if pointer2.next is None else pointer2.next.next

        return False
