class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLenStr = math.inf
        match = True
        res = ""
        for s in strs:
            minLenStr = min(minLenStr, len(s))
        
        i=0   
        while i<minLenStr and match:
            c = strs[0][i]
            for s in strs:
                if s[i]!=c:
                    match = False
            if match:
                res = res + strs[0][i]
            i+=1
        return res
                
                
                    
        