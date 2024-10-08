class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s):1}
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                memo[i] = 0
            else:
                memo[i] = memo[i+1]
            if i+1<len(s) and (s[i] =="1" or (s[i]=="2" and s[i+1] in "0123456")):
                memo[i]= memo[i] + memo[i+2]
        return memo[0]
                                   
                                  
        