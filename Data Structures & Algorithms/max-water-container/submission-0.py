class Solution:
    def maxArea(self, height: List[int]) -> int:
        currMax = 0
        size = len(height)
        l ,r=0 ,size-1
        while l<r:
            # Area calculate karo: min(height[L], height[R]) * (R - L)
            currMax = max(currMax,min(height[l],height[r])*(r-l))
            # Kaunsi wall hatai jaye?
            # Jo wall choti hai, use andar lao (L++ ya R--).
            if min(height[l],height[r]) == height[l]:
                l+=1
            else:
                r-=1
        
        return currMax

height = [1,8,6,2,5,4,8,3,7]
obj=Solution()
soln=obj.maxArea(height)
print(soln)
        
