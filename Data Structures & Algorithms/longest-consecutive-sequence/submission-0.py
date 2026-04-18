class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        numset=set(nums)
        for n in nums:
            if (n-1) not in numset:
                counter = 1
                while (n+counter) in numset:
                    counter+=1
                longest = max(longest,counter)
        return longest

nums = [2,20,4,10,3,4,5]
obj=Solution()
soln=obj.longestConsecutive(nums)
print(soln)