class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # Isme hum indices store karenge, values nahi!

        for i, temp in enumerate(temperatures):
            # Jab tak stack khali nahi hai aur aaj ka temp purane din se bada hai
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index  # Days ka difference
            
            # Aaj ka index push kardo taaki ye aage aane wale warmer din ka wait kare
            stack.append(i)

        return res

temperatures = [30,38,30,36,35,40,28]
obj = Solution()
soln = obj.dailyTemperatures(temperatures)
print(soln)