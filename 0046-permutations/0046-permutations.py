class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def backtrack(curRes, remArr):
            print(curRes, remArr)
            if len(remArr)==1:
                curRes.append(remArr[0])
                res.append(curRes.copy())
                curRes.pop()
                return
            for i in range(len(remArr)):
                curRes.append(remArr[i])
                backtrack(curRes, remArr[:i:]+remArr[i+1::])
                curRes.pop(-1)
        backtrack([],nums)
        return res