class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# Treat the array like a linked list where each value points to the next index.
# Use Floyd's cycle detection to find the cycle created by the duplicate number,
# then reset one pointer to the start and move both at the same speed to find
# the duplicate value.
# Time: O(n), Space: O(1)