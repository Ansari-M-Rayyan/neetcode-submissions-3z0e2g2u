# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # 1. Calculate the total length of the list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        # 2. Advance to the node right before the one to remove
        steps_to_target = length - n
        curr = dummy
        for _ in range(steps_to_target):
            curr = curr.next

        # 3. Bypass the target node
        curr.next = curr.next.next

        return dummy.next

# Use a dummy node to handle edge cases, calculate the list length, then find
# the node just before the Nth node from the end and bypass it.
# Time: O(n), Space: O(1)