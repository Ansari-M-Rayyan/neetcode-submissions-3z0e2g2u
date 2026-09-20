class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1

        while l < r:
            mid = ( l + r ) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]  

obj = Solution()
nums = [3,4,5,6,1,2]
soln = obj.findMin(nums)
print(soln)

# Basically, we have two cases: 
# either midpoint is greater than OR equal to the LAST NUMBER. 
# If it's greater than, then that means a number is somewhere in the right side of midpoint, 
# therefore, we do l = mid + 1

# BUT IF midpoint is LESS THAN the last number, then set the right boundary or r = mid