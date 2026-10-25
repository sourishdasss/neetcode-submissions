class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            
            # processing a number
            else:
                stack.append(int(t))

            # print(stack)
        
        return stack[0]