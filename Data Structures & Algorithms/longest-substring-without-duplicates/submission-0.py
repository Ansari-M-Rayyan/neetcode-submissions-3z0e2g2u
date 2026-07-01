class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1

            charSet.add(s[r])
            res = max(res ,r - l + 1)
        return res

s = "zxyzxyz"
obj = Solution()
soln = obj.lengthOfLongestSubstring(s)
print(soln)

# Sliding Window:
# Expand right pointer, shrink left on duplicates, and track the longest unique substring.
# Time: O(n), Space: O(min(n, charset))