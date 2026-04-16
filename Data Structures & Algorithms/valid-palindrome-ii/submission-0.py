class Solution:
    def validPalindrome(self, s: str) -> bool:
        size=len(s)
        l ,r =0 ,size-1
        
        def check(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return check(l+1,r) or check(l,r-1)
        return True


s = "adf"
obj=Solution()
soln=obj.validPalindrome(s)
print(soln)
