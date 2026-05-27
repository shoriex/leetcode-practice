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
# Strategy 1. Check all nodes from head and save the nodes to recognize the node has been already visited.
# If duprication occurs, the list has circle. 
# This approach is easy to implement but it requires O(n) space complexity.


# Strategy 2. Use two pointers that speeds are diffrent. First pointer moves 1 node in 1 step
# and second pointer moves 2 nodes in 1 step.
# This approach is a bit tricky but it requires O(1) space complexity.

# Example. A -> B -> C -> D -> A
# First Pointer:  A -> B -> C -> D
# Second Pointer: B -> D -> B -> D

from typing import Optional


class Solution:

    # Strategy 1
    def hasCycle1(self, head: Optional["ListNode"]) -> bool:
        visited_node = set()
        while(head is not None):
            # 1. Check the node is already visited
            if head in visited_node:
                return True
            # 2. Save the current node.
            visited_node.add(head)

            # 3. Move head pointer
            head = head.next

        return False

    # Strategy 2
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        # init
        if head is None:
            return False
        pointer1 = head
        pointer2 = pointer1.next

        while(1):
            # 1. Check if the pointer is valid
            if pointer2 is None:
                return False
            
            # 2. Check if the two pointers are same
            if pointer1 == pointer2:
                return True
            
            # 3. Update pointer head
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            if pointer2 is None:
                return False
            pointer2 = pointer2.next
