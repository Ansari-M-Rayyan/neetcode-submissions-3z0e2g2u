class Solution:
    def findDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return num

            seen.add(num)

nums = [1, 2, 3, 2, 2]
print(Solution().findDuplicate(nums))

'''
HashSet:
Time  = O(n)
Space = O(n)

Floyd's:
Time  = O(n)
Space = O(1)
'''