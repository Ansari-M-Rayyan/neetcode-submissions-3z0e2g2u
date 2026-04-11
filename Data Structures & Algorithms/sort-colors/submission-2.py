class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        low=0   # keep track of '0' (points the last '0' elem)
        mid=0   # traverse the complete list
        high=size-1 # keep track of '2' (points the initial(latest) '2' elem)

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