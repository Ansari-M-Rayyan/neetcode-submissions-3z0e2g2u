# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev ,curr = None ,head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

# Reverse the linked list iteratively by changing each node's next pointer
# to point to the previous node, while keeping track of the next node.
# Continue until all nodes are reversed, then return the new head.
# Time: O(n), Space: O(1)