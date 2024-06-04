#https://www.youtube.com/watch?v=cTBiBSnjO3c&t=611s
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res =[0] * len(temperatures)
        tempStack =[[temperatures[0],0]]
        for i in range(1,len(temperatures)):
            while len(tempStack)>0 and temperatures[i]>tempStack[-1][0]:
                res[tempStack[-1][1]] = i - tempStack[-1][1]
                tempStack.pop()
            tempStack.append([temperatures[i],i])
        return res