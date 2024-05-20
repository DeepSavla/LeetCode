class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        prev_sign = "+" 
        s=s.replace(" ","")
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                if not stack or stack[-1] not in ["*", "/"]:
                    if prev_sign == "+":
                        stack.append(num)
                    else:
                        stack.append(-num)
                else:
                    operator = stack.pop()
                    num1 = stack.pop()
                    if operator == "*":
                        tmp = num1 * num
                    else:
                        tmp = int(num1 / num)
                    stack.append(tmp)
            else:
                if s[i] == "+":
                    prev_sign = "+"
                elif s[i] == "-":
                    prev_sign = "-"
                else:
                    stack.append(s[i])
                i += 1
        return sum(stack)