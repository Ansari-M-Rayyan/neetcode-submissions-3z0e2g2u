class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                y = stack.pop()
                x = stack.pop()

                match token:
                    case '+': 
                        res = x + y
                    case '-': 
                        res = x - y
                    case '*': 
                        res = x * y
                    case '/': 
                        res = int(x / y)
                
                stack.append(res)
                
            else: 
                stack.append(int(token))
        
        return stack[0]

obj = Solution()
tokens = ["1","2","+","3","*","4","-"]
soln = obj.evalRPN(tokens)
print(soln)