class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l ,r= 1 ,max(piles)
        res = r

        while l <= r:

            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res ,k)
                r = k - 1
            else:
                l = k + 1
        
        return res

obj = Solution()
piles = [1,4,3,2]
h = 9
soln = obj.minEatingSpeed(piles ,h)
print(soln)

# Use binary search to find the minimum eating speed that allows all bananas
# to be eaten within h hours.
# For each speed, calculate the total hours needed.
# If the speed is sufficient, search for a smaller speed; otherwise, search higher.
# Time: O(n log(max(piles))), Space: O(1)