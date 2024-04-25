class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res=0
        for t in tokens:
            if t in "+-*/":
                dig1=int(stack.pop())
                dig2=int(stack.pop())
                if t == "+":
                    res = dig2 + dig1
                elif t == "-":
                    res = dig2 - dig1
                elif t == "*":
                    res = dig2 * dig1
                else:
                    res = dig2/dig1
                stack.append(res)
            else:
                stack.append(t)
                res = int(t)
        return int(res)