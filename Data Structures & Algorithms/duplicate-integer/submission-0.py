class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sizeLst=len(nums)
        sizeUnqiue=len(list(set(nums)))
        if sizeLst != sizeUnqiue:
            return  True
        return False

nums = [1, 2, 3, 3]
obj=Solution()
soln=obj.hasDuplicate(nums)
print(soln)
            
        