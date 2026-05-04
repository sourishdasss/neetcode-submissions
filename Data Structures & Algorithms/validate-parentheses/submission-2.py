class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        if len(s) % 2 != 0: return False

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)

            elif c == ')' or c == ']' or c == '}':
                if stack:
                    opening_bracket = stack.pop()
                    if c == ')' and opening_bracket == '(':
                        continue
                    elif c == ']' and opening_bracket == '[':
                        continue
                    elif c == '}' and opening_bracket == '{':
                        continue
                    else:
                        return False
                else:
                    return False

        print(stack)

        if stack:
            return False

        return True
        
        
        