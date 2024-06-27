class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = {}
        for l in s:
            if l in hm.keys():
                hm[l] +=1
            else:
                hm[l] =1
        totalLen = 0
        oddEncountered = False
        for k in hm.keys():
            if hm[k]%2==0:
                totalLen = totalLen + hm[k]
            else:
                    totalLen = totalLen + hm[k] -1
                    oddEncountered = True
        if oddEncountered:
            return totalLen+1
        return totalLen
                
            
            
            
            
        