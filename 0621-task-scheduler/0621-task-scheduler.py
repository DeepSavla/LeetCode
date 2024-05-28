class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = {}
        hmCooling ={}
        minRunTime = 0
        for t in tasks:
            if t in hm.keys():
                hm[t] +=1
            else:
                hm[t]=1
                hmCooling[t] = 0
        while len(hm)!=0:
            taskPriority = heapq.nlargest(n+1,hm.keys(),key=hm.get)
            lastAdded = None
            for t in taskPriority:
                if hmCooling[t] ==0:
                    hmCooling[t] = n
                    lastAdded = t
                    if hm[t] == 1:
                        del hm[t]
                    else:
                        hm[t] = hm[t] - 1
                    break
            minRunTime+=1
            for c in hmCooling:
                if c!=lastAdded and hmCooling[c]!=0:
                    hmCooling[c] -=1
        return minRunTime
        
        
        
        
        
                