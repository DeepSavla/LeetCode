class Solution:
    def minimumKeypresses(self, s: str) -> int:
        hm = {}
        occ = {1:9 , 2: 9 , 3:9}
        count =0
        for let in s:
            if let in hm.keys():
                hm[let] = hm[let]+1
            else:
                hm[let] = 1
        while len(hm):
            maxOccChar = heapq.nlargest(1,hm.keys(),key=hm.get)
            if occ[1]>0:
                count =count+ hm[maxOccChar[0]]
                occ[1] = occ[1] - 1
            elif occ[2]>0:
                count =count+ (hm[maxOccChar[0]]*2)
                occ[2] = occ[2] - 1
            else:
                count =count+ (hm[maxOccChar[0]]*3)
            del hm[maxOccChar[0]]
        return count