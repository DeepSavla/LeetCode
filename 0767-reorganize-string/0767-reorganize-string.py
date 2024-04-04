import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        hm = {}
        for letter in s:
            if letter not in hm.keys():
                hm[letter]=1
            else:
                hm[letter] = hm[letter] +1
                
        resStr= ""
        prevChar = None
        while len(hm) > 0:
            maxFreq = heapq.nlargest(2,hm.keys(),key=hm.get)
            if len(hm)==1 and hm[maxFreq[0]]>1: #for null string case
                return ""
            if maxFreq[0] == prevChar and prevChar !=None: #none for first case
                currChar = maxFreq[1]
            else:
                currChar = maxFreq[0]
            resStr += currChar
            prevChar = currChar
            if hm[currChar] > 1:
                hm[currChar] = hm[currChar]-1
            else:
                del hm[currChar]
        return resStr