class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        size = len(nums)
        
        for i in range(size - 2):
            # 1. Skip duplicate 'a'
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l = i + 1
            r = size - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 2. Skip duplicate 'b' (Most Important!)
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    # 3. Skip duplicate 'c'
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res
nums = [-1,0,1,2,-1,-4]
obj=Solution()
soln=obj.threeSum(nums)
print(soln)
                