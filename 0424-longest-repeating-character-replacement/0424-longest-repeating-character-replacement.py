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
        while i<len(s):
            if j-i+1-maxCount(hm)<=k and j<len(s)-1:
                j=j+1
                if s[j] in hm:
                    hm[s[j]] +=1
                else:
                    hm[s[j]] =1
            else:
                print(hm)
                print(i,j)
                if hm[s[i]]==1:
                    del hm[s[i]]
                else:
                    hm[s[i]] -=1
                i=i+1
            if j-i+1-maxCount(hm)<=k:
                maxLen = max(j-i+1,maxLen)
        return maxLen