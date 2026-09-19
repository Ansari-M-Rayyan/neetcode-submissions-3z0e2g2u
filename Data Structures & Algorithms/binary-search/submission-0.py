class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l ,r = 0 ,len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m -1
            else:
                return m
        return -1
    
obj = Solution()
nums = [-1,0,3,4,6,8]
target = 6
soln = obj.search(nums ,target)
print(soln)

# This is a simple binary search problem where we just recursively follow divide & conquer strategy to get to the solution.
# here we can also calculate mid by simply doing : m = (l + r)//2
# but we follow the above due to overflow problem many other prog lang. have (not python) where l + r might reach 2^32 and gone overflow.
# m = l + ((r - l) // 2)
# (r - l) : <final - initial> gives the length between l & r
# (r - l) // 2 : divided the total length by 2 so we got the half of the length.
# l + ((r - l) // 2) : then we add that 'half' to 'l' so we get the mid point.
# This is how we don't have any overflow problem ,because we didn't directly did "l + r"