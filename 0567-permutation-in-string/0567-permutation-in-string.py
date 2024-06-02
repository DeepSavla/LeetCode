class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # High level algo:
        # window size is len(S1)
        # check in every window if s1 and s2 are same
        winLen = len(s1)
        i=0
        j=winLen-1
        hm1 = {}
        hm2 ={}
        if winLen>len(s2):
            return False
        for idx in s1:
            if idx in hm1:
                hm1[idx] +=1
            else:
                hm1[idx]=1
        for idx in range(j+1):
            if s2[idx] in hm2:
                hm2[s2[idx]]+=1
            else:
                hm2[s2[idx]]=1
        if hm1==hm2:
                return True
        while j<len(s2)-1:
            hm2[s2[i]] -=1
            if hm2[s2[i]]==0:
                del hm2[s2[i]]
            i+=1
            j+=1
            if s2[j] in hm2:
                hm2[s2[j]] +=1
            else:
                hm2[s2[j]]=1
            if hm1==hm2:
                return True
        return False
            
            
        
        