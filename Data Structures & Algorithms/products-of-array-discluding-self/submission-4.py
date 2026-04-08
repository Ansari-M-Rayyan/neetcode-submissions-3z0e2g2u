class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodP=1
        lstP=[1]
        for i in range(len(nums)-1):
            prodP=nums[i]*prodP
            lstP.append(prodP)
        
        prodS=1
        lstS=[1]
        for i in range(len(nums)-1,0,-1):
            prodS=nums[i]*prodS
            lstS.append(prodS)
        lstS.reverse()
        retLst=[x*y for x,y in zip(lstS,lstP)]
        return retLst

nums = [1,2,4,6]
obj=Solution()
soln=obj.productExceptSelf(nums)
print(soln)