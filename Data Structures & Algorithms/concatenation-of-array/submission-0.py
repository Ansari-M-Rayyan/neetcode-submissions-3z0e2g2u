class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(0,len(nums)):
            ans.append(nums[i])
        return ans+nums

nums = [1,4,1,2]
obj = Solution()
soln = obj.getConcatenation(nums)
print(soln)