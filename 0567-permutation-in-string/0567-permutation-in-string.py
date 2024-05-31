class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # High level algo:
        # window size is len(S1)
        # check in every window if s1 and s2 are same
        winLen = len(s1)
        i=0
        j=winLen-1
        sortedStr = sorted(s1)
        while j<len(s2):
            if sortedStr == sorted(s2[i:j+1]):
                return True
            i+=1
            j+=1
        return False
            
        
        