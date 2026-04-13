class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        cmax = 0
        
        for n in nums:
            if n == 1:
                count += 1
                # Har baar count update karte hi max check kar lo
                # Isse loop ke bahar wala extra 'if' bach jayega
                cmax = max(cmax, count)
            else:
                count = 0
        return cmax

nums = [1,1,0,1,1,1]
obj=Solution()
soln=obj.findMaxConsecutiveOnes(nums)
print(soln)
            
            
        