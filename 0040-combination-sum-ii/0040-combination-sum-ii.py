class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        def backtrack(i,subarr,total):
            if total==target:
                res.append(subarr.copy())
                return
            if i==len(candidates) or total>target:
                return
            subarr.append(candidates[i])
            total = total+candidates[i]
            backtrack(i+1,subarr,total)
            subarr.pop()
            total = total-candidates[i]
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(i+1,subarr,total)
        backtrack(0,[],0)
        return res
                
        