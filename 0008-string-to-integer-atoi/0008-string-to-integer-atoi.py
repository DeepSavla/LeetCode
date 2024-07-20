class Solution:
    def myAtoi(self, s: str) -> int:
        ans  = 0
        isPositive = True
        i = 0
        if s=="":
            return 0
        while i<len(s) and s[i] == ' ':
            i += 1
        
        if i<len(s) and s[i] in '+-':
            if s[i] == "-":
                isPositive = False
            i+=1
        
        
        while i<len(s) and ord(s[i]) in range(48, 58):
            x = ord(s[i]) - 48
            ans = ans*10 + x 
            i += 1
            if i == len(s):
                break
                
        if isPositive == False:
            ans= -ans
        if ans > 2**31 -1:
            ans = 2**31 -1
        if ans < -2**31:
            ans = -2**31
        return ans