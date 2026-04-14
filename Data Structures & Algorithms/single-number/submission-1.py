class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            res = res ^ num

        return res

nums=[2,2,1]
obj=Solution()
soln=obj.singleNumber(nums)
print(soln)

# Previous submission was having Time : O(n) ,but Space : O(n) due to dictionary used

# This soln is having Time : O(n) & Space : O(1)