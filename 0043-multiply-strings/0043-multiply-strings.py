class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        sum = 0
        i=len(num2)-1
        while i>=0:
            curDigRes = int(num2[i]) * num1
            curDigRes = curDigRes * (10**((len(num2)-1)-i))
            print(curDigRes)
            sum = sum+ curDigRes
            i-=1
        return str(sum)
        