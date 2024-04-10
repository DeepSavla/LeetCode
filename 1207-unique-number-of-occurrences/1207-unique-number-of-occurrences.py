class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = {}
        for n in arr:
            if n in hm.keys():
                hm[n] = hm[n]+1
            else:
                hm[n]=1
        occSet = set()
        for key in hm.keys():
            l = len(occSet)
            occSet.add(hm[key])
            if l == len(occSet):
                return False
        return True