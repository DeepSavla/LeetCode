class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        numLen = len(s)
        hm ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        #trick: if current roman is smaller than the next roman character, then we need to substract that value from next character. Else, add it
        for i in range(numLen):
            if i+1!=numLen and hm[s[i+1]] > hm[s[i]]:
                res = res-hm[s[i]]
            else:
                res = res+hm[s[i]]
        return res