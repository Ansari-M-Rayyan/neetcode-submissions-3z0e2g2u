class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        """ this is kadane's algorithm """
        global_max = float('-inf')
        local_max = 0

        """ For each element, you must make a simple decision: 
        do you add the current element to the existing subarray, 
        or start a brand new subarray starting at the current element? 
        You reset the current subarray sum to 0 (or to the current element, 
        depending on the variation) whenever its value drops below zero, 
        because a negative sum will only drag down future numbers. """

        for no in nums:
            local_max += no

            if local_max > global_max :
                global_max = local_max
            
            if local_max < 0 :
                local_max = 0

        return global_max

obj = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
soln = obj.maxSubArray(nums)
print(soln)