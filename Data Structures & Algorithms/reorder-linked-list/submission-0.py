# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Fast & Slow pointers se mid find karo
        slow = head
        fast = head.next  # fast ko head.next se start karne par slow first half ke end par rukta hai

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Second half ka head slow.next hoga
        second = slow.next
        slow.next = None  # Dono halves ko disconnect kardo

        # Step 2: Second half ko reverse karo
        prev = None
        curr = second

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # 'prev' ab reversed second half ka naya head hai
        second = prev

        # Step 3: Dono halves ko alternate merge karo
        first = head
        while second:
            # Agle pointers temporarily store karo
            tmp1 = first.next
            tmp2 = second.next

            # Weaving connections:
            first.next = second
            second.next = tmp1

            # Pointers ko aage move karo
            first = tmp1
            second = tmp2

"""
1. List ka middle dhoondhna ( Fast & Slow Pointers )
2. List ke second half ko ulta karna ( Reverse Linked List )
3. Dono halves ko alternate weave/merge karna ( Zip / Merge Two Lists )
"""