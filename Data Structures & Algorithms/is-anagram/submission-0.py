class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strS=''.join(sorted(s))
        strT=''.join(sorted(t))
        if strS==strT:
            return True
        return False

s = "racecar"
t = "carrace"
obj=Solution()
soln=obj.isAnagram(s,t)
print(soln)