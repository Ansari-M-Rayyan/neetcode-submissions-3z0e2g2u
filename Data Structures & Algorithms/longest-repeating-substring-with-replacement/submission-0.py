class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r] ,0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -=1
                l +=1

            res = max(res ,r - l + 1)
        return res

s = "XYYX"
k = 2
obj = Solution()
soln = obj.characterReplacement(s ,k)
print(soln)

# Sliding Window + Frequency Map
# Expand the window right side while counting character frequencies.

# If replacements needed (window size - highest frequency) > k, shrink from the left.
# Track the maximum valid window length.

# Time: O(26 * n) ≈ O(n) for uppercase letters, Space: O(26) ≈ O(1)