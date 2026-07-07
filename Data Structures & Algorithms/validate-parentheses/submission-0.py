class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ')' : '(' ,
            '}' : '{' ,
            ']' : '['
        }

        for i in s:
            if i in closeToOpen:

                topElem = stack.pop() if stack else "#"
                if topElem != closeToOpen[i]:
                    return False
            
            else:
                stack.append(i)

        return True if not stack else False

s = "[]"
obj = Solution()
soln = obj.isValid(s)
print(soln)

'''
1. Opening bracket → Push onto stack.
2. Closing bracket → Pop and compare.
3. Mismatch or empty stack → False.
4. Empty stack at the end → True.

Time: O(n), Space: O(n)
'''