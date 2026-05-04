class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")  
        stack = []


        print(dirs)

        for d in dirs:
            if d == "" or d == ".":
                continue
            elif d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        
        print(stack)
        output = "/"
        for s in stack:
            if output != "/":
                output += "/"
            output += s
        print(output)

        return output

