import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodLst=[]
        for i in range(len(nums)):
            temp=nums[:]
            ignoredItem=temp.pop(i)
            prodLst.append(math.prod(temp))
        return prodLst

nums = [1,2,4,6]
obj=Solution()
soln=obj.productExceptSelf(nums)
print(soln)