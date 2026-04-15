class Solution:
    def isPalindrome(self, s: str) -> bool:
        l ,r=0 ,len(s)-1    # l=0 ,r=27

        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True

s = "Was it a car or a cat I saw?"
obj=Solution()
soln=obj.isPalindrome(s)
print(soln)

# Logic:

# left pointer shuru mein, right pointer aakhir mein.

# Agar left pointer par koi faltu character (comma, space) hai, toh use skip karo (left += 1).

# Agar right pointer par faltu character hai, toh use skip karo (right -= 1).

# Jab dono pointers valid characters par hon, tab unhe compare karo.