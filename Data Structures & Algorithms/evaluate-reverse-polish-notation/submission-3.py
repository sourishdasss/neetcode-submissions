class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": "+",
            "-": "-",
            "*": "*",
            "/": "/",
        }

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                operator = operators[t]

                if operator == "+":
                    new = num1 + num2
                    stack.append(new)
                elif operator == "-":
                    new = num1 - num2
                    stack.append(new)
                elif operator == "*":
                    new = num1 * num2
                    stack.append(new)
                else:
                    new = int(num1 / num2)
                    stack.append(new)
            print(stack)
        return stack[-1]
