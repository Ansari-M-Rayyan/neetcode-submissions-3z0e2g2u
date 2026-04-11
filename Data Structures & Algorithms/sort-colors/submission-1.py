class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        low=0
        mid=0
        high=size-1

        for i in range(size):
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1

            elif nums[mid]==2:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
            
            else: # nums[mid]==1
                mid+=1


nums = [1,0,1,2]
obj=Solution()
soln=obj.sortColors(nums)
print(soln)