# https://www.youtube.com/watch?v=gqXU1UyA8pk&t=431s
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def maxCount(hm):
            max = 0
            for k in hm.keys():
                if hm[k]> max:
                    max = hm[k]
            return max
        
        hm = {s[0]:1}
        i=0
        j=0
        maxLen = 1
        while j<len(s)-1:
            if j-i+1-maxCount(hm)<=k:
                j=j+1
                if s[j] in hm:
                    hm[s[j]] +=1
                else:
                    hm[s[j]] =1
            else:
                if hm[s[i]]==1:
                    del hm[s[i]]
                else:
                    hm[s[i]] -=1
                i=i+1
            if j-i+1-maxCount(hm)<=k:
                maxLen = max(j-i+1,maxLen)
        return maxLen