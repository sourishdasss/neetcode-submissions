class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        for p in s:
            if p not in close:
                stack.append(p)
            else:
                if stack and stack[-1] == close[p]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        
        return False