class Solution(object):
    def isValid(self, s):
        stack = []
        for line in s:
            if line in "({[":
                stack.append(line)
            if line in "}])":
                if (len(stack) > 0 and line == "]" and stack[-1] == "["):
                    stack.pop()
                elif (len(stack) > 0 and line == "}" and stack[-1] == "{"):
                    stack.pop()
                elif (len(stack) > 0 and line == ")" and stack[-1] == "("):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False