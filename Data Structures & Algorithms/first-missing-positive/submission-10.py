class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=1
        numSet = set(nums)
        size=len(numSet)
        for i in range(size):
            if n in numSet:
                n=n+1
        return n

nums = [1,2,4]
obj=Solution()
soln=obj.firstMissingPositive(nums)
print(soln)
        