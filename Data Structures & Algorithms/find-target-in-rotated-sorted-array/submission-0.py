class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid

            # Check karo kaunsa half sorted hai
            
            # Left half sorted hai:
            if nums[l] <= nums[mid]:
                # Kya target left sorted half ke daayre mein aata hai?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # Right half sorted hai:
            else:
                # Kya target right sorted half ke daayre mein aata hai?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1  

        return -1

obj = Solution()
nums = [3,4,5,6,1,2]
target = 1
soln = obj.search(nums ,target)
print(soln)


# Use binary search on the rotated sorted array.
# At each step, identify which half is sorted, then check whether the target
# lies within that sorted range. Search that half if it does; otherwise search
# the other half.
# Time: O(log n), Space: O(1)
