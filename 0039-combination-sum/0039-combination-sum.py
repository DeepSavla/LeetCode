class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i,curRes):
            if sum(curRes) ==target:
                res.append(curRes.copy())
                return
            if i>= len(candidates) or sum(curRes) > target:
                return
            curRes.append(candidates[i])
            backtrack(i,curRes)
            curRes.pop()
            backtrack(i+1,curRes)
        backtrack(0,[])
        return res
        
        