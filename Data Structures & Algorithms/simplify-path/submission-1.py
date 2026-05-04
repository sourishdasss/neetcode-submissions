class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")  
        stack = []

        # for d in dirs:
        #     if d == "" or d == ".":
        #         continue
        #     elif d == "..":
        #         if stack:
        #             stack.pop()
        #     else:
        #         stack.append(d)

        curr = ""
        for c in path:
            if c != "/":
                curr += c
            elif c == "/":
                if curr != "":
                    stack.append(curr)
                    curr = ""
        if curr:
            stack.append(curr)

        print(stack)
        final = []
        for s in stack:
            if s == "..":
                if final:
                    final.pop()
            elif s == ".":
                continue
            else:
                final.append(s)
        
        output = "/"
        for s in final:
            if output != "/":
                output += "/"
            output += s

        return output

