class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        curStr = "1"
        count = 0
        for i in range(2,n+1):
            newStr=""
            lenCurStr = len(curStr)
            for j in range(lenCurStr):
                count+=1
                if j==lenCurStr-1 or curStr[j] != curStr[j+1]:
                    newStr = newStr + str(count) + curStr[j]
                    count = 0   
            curStr = newStr
        return curStr