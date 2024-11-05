class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(i,arr,curStr):
            if i>=len(s) and len(arr)==4:
                res.append(".".join(arr))
                return
            if len(arr)>4 or i>=len(s):
                return
            curStr = curStr +s[i]
            if (len(curStr)>1 and curStr[0] == '0') or int(curStr)>255:
                return
            arr.append(curStr)
            backtrack(i+1,arr,"")
            arr.pop()
            
            if i + 1 < len(s):
                backtrack(i+1, arr, curStr)
            
            
        
        backtrack(0,[],"")
        return res
        