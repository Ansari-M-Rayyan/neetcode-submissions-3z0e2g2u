class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i] ,0)
            window_count[s2[i]] = 1 + window_count.get(s2[i] ,0)

        if s1_count == window_count:
            return True

        l = 0
        for r in range(len(s1) ,len(s2)):
            window_count[s2[r]] = 1 + window_count.get(s2[r] ,0)

            window_count[s2[l]] -= 1

            if window_count[s2[l]] == 0:
                del window_count[s2[l]]

            l += 1

            if s1_count == window_count:
                return True

        return False

s1 = "abc" 
s2 = "lecabee"
obj = Solution()
soln = obj.checkInclusion(s1 ,s2)            
print(soln)

'''
Window Size = len(s1)
1. Build frequency map of s1.
2. Build frequency map of the first window in s2.
3. Slide the window:
   - Add incoming character.
   - Remove outgoing character.
   - Compare frequency maps.
4. If maps match → permutation found.
'''