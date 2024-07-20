class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        i=0
        if s=="":
            return 0
        while i<len(s) and s[i]==" ":
            i+=1
        if i<len(s) and s[i] in "+-":
            if s[i] =="+":
                sign = 1
            else:
                sign = -1
            i+=1
        for j in range(i,len(s)):
            if s[j]==" " or s[j] in "+-":
                break
            elif ord(s[j])>=48 and ord(s[j])<=57:
                res = res*10 + (ord(s[j])-48)
            else:
                break
        res = res*sign
        if res>(2**31-1):
            res = 2**31-1
        if res< -2**31:
            res = -2**31
        return res
        