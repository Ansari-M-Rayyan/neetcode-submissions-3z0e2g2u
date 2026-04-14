class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            res = res ^ num    # using xor logic that cancels same numbers (ie., 2 XOR 2 = 0 ,then 0 XOR 1 = 1)

        return res

nums=[2,2,1]
obj=Solution()
soln=obj.singleNumber(nums)
print(soln)

# Previous submission was having Time : O(n) ,but Space : O(n) due to dictionary used

# This soln is having Time : O(n) & Space : O(1)
