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
        prevChar = None
        while len(hm) > 0:
            maxFreq = heapq.nlargest(2,hm.keys(),key=hm.get)
            if len(hm)==1 and hm[maxFreq[0]]>1: #for null string case
                return ""
            if prevChar == None:
                currChar = maxFreq[0]
            else:
                if maxFreq[0] == prevChar:
                    currChar = maxFreq[1]
                else:
                    currChar = maxFreq[0]
            resArr.append(currChar)
            prevChar = currChar
            if hm[currChar] > 1:
                hm[currChar] = hm[currChar]-1
            else:
                del hm[currChar]
        resStr =""
        resStr = resStr.join(resArr)
        return resStr