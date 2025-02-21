class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        def backtrack(i,subarr):
            total = sum(subarr)
            if total==target:
                res.append(subarr.copy())
                return
            if i==len(candidates) or total>target:
                return
            subarr.append(candidates[i])
            backtrack(i+1,subarr)
            subarr.pop()
            total = total-candidates[i]
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(i+1,subarr)
        backtrack(0,[])
        return res
                
        