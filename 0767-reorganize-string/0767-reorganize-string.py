import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        hm = {}
        for letter in s:
            if letter not in hm.keys():
                hm[letter]=1
            else:
                hm[letter] = hm[letter] +1
        resArr=[]
        while len(hm) > 0:
            maxFreq = heapq.nlargest(2,hm.keys(),key=hm.get)
            if len(hm)==1 and hm[maxFreq[0]]>1: #for null string case
                return ""
            if len(resArr) == 0:
                resArr.append(maxFreq[0])
                if hm[maxFreq[0]] > 1:
                    hm[maxFreq[0]] = hm[maxFreq[0]]-1
                else:
                    del hm[maxFreq[0]]
                continue    #imp
            if maxFreq[0] == resArr[-1]:
                resArr.append(maxFreq[1])
                if hm[maxFreq[1]] > 1:
                    hm[maxFreq[1]] = hm[maxFreq[1]]-1
                else:
                    del hm[maxFreq[1]]
            else:
                resArr.append(maxFreq[0])
                if hm[maxFreq[0]] > 1:
                    hm[maxFreq[0]] = hm[maxFreq[0]]-1
                else:
                    del hm[maxFreq[0]]
        resStr =""
        resStr = resStr.join(resArr)
        return resStr
            #check previous character for empty string