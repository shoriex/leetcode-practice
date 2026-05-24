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
