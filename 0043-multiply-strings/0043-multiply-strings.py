class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        sum = 0
        num2 = num2[::-1]
        print(num2)
        for i in range(len(num2)):
            curVal = int(num2[i])*num1
            curVal = (10**i)*curVal
            sum = sum + curVal
        return str(sum)
        