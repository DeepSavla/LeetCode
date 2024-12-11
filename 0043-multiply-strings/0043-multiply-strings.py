class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        sum = 0
        num2Idx = len(num2)-1
        i = num2Idx
        while i>=0:
            curDigRes = int(num2[i]) * num1
            curDigRes = curDigRes * (10**(num2Idx-i))
            print(curDigRes)
            sum = sum+ curDigRes
            i-=1
        return str(sum)
        