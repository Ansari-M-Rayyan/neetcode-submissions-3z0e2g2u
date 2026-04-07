import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        floor_val=math.floor(len(nums)/2)       # 3
        nums.sort()        # [1,1,1,5,5,5,5]
        count=1
        len_lst=len(nums)   # 7
        x=0
        i=0
        if len_lst==1:
            return nums[0]
        while i< (len_lst-1):
            if nums[i]==nums[i+1]:
                count+=1
                i+=1
            else:
                count=1
                i+=1
            if count>floor_val:
                return nums[i]
            x+=1

nums = [5,5,1,1,1,5,5]
obj=Solution()
soln=obj.majorityElement(nums)
print(soln)