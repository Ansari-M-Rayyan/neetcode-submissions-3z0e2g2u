class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numFreq={}  # format : {number:frequency}

        for num in nums:
            numFreq[num] = numFreq.get(num,0) + 1
        
        for k,v in numFreq.items():
            if v==1:    # becoz freq is our value
                return k

nums=[2,2,1]
obj=Solution()
soln=obj.singleNumber(nums)
print(soln)