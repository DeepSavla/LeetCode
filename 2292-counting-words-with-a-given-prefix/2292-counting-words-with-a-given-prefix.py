class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        total = 0
        for w in words:
            if len(w)<len(pref):
                continue
            for i in range(len(pref)):
                if pref[i] != w[i]:
                    break
                if i == len(pref)-1:
                    total +=1
        return total
            
                

        