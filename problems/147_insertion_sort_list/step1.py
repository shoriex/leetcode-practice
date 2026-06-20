#              ↓
# nodes: [1, | 7, 5, 9, 10]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        sorted_last_node = head
        unsorted_first_node = head.next
        while unsorted_first_node is not None:
            if sorted_last_node.val <= unsorted_first_node.val:
                sorted_last_node = sorted_last_node.next
                unsorted_first_node = unsorted_first_node.next
                continue

            insert_target = unsorted_first_node

            unsorted_first_node = unsorted_first_node.next
            sorted_last_node.next = unsorted_first_node

            pre = None
            curr = head
            while True:
                if insert_target.val <= curr.val:
                    insert_target.next = curr
                    if pre is not None:
                        pre.next = insert_target
                    else:
                        head = insert_target
                    break

                pre = curr
                curr = curr.next

        return head
