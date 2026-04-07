class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        # Step 1: Left se Right jao (Prefix Product)
        # res[i] mein i se pehle waale saare numbers ka product hoga
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Right se Left jao (Suffix Product)
        # Ab jo res[i] pehle se hai, usmein right side ka product multiply kar do
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res

# Testing
nums = [1, 2, 4, 6]
obj = Solution()
print(obj.productExceptSelf(nums)) # Output: [48, 24, 12, 8]