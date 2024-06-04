class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        if n==2:
            return "11"
        curStr = "11"
        count = 0
        for i in range(3,n+1):
            newStr=""
            for j in range(len(curStr)):
                if j!=len(curStr)-1 and curStr[j] == curStr[j+1]:
                    count+=1
                else:
                    count+=1
                    newStr = newStr + str(count) + curStr[j]
                    count = 0
            curStr = newStr
        return curStr
                
            
        