# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # [1, 7, 3, 2, 5]
        if head is None:
            return head

        sorted_last_node = head
        unsorted_first_node = head.next

        while unsorted_first_node is not None:
            if sorted_last_node.val <= unsorted_first_node.val:
                sorted_last_node = sorted_last_node.next
                unsorted_first_node = unsorted_first_node.next
                continue

            target = unsorted_first_node
            sorted_last_node.next = unsorted_first_node.next
            unsorted_first_node = unsorted_first_node.next

            pre = None
            curr = head
            while True:
                if target.val <= curr.val:
                    target.next = curr
                    if pre is not None:
                        pre.next = target
                    else:
                        head = target
                    break
                pre = curr
                curr = curr.next

        return head
