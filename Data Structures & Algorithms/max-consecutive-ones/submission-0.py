class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        cmax=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            elif nums[i]==0:
                if count>cmax:
                    cmax=count
                count=0
        if count>cmax:
            cmax=count
        return cmax

nums = [1,1,0,1,1,1]
obj=Solution()
soln=obj.findMaxConsecutiveOnes(nums)
print(soln)
            
            
        