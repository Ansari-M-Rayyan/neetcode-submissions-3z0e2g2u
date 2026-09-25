# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Loop tab tak chalega jab tak l1 bacha ho, l2 bacha ho, ya koi aakhri carry bacha ho
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Sum calculate karo
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Naya node attach karo
            curr.next = ListNode(digit)
            curr = curr.next

            # Pointers aage badhao (agar node exist karta hai)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

# Add the two numbers digit by digit while traversing both linked lists.
# Track the carry from each addition and create a new node for each resulting
# digit. Continue until both lists and the final carry are processed.
# Time: O(max(n, m)), Space: O(max(n, m))