class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        numLen = len(s)
        i=0
        hm ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        while i<numLen:
            if s[i]=="I" and i<numLen-1:
                if s[i+1] == "V":
                    res = res+4
                    i+=2
                elif s[i+1] == "X":
                    res = res+9
                    i+=2
                else:
                    res = res+hm[s[i]]
                    i+=1
            elif s[i]=="X" and i<numLen-1:
                if s[i+1] == "L":
                    res = res+40
                    i+=2
                elif s[i+1] == "C":
                    res = res+90
                    i+=2
                else:
                    res = res+hm[s[i]]
                    i+=1
            elif s[i]=="C" and i<numLen-1:
                if s[i+1] == "D":
                    res = res+400
                    i+=2
                elif s[i+1] == "M":
                    res = res+900
                    i+=2
                else:
                    res = res+hm[s[i]]
                    i+=1
            else:
                res = res+hm[s[i]]
                i+=1
        return res