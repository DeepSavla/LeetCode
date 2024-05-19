class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack =[]
        res = ""
        for i in path:
            if i==".." and len(stack)>0:
                stack.pop()
            elif len(i)>0 and i!="." and i!="..":
                stack.append(i)
        if len(stack)==0:
            return "/"
        for i in stack:
            res = res + "/" + i
        return res
            