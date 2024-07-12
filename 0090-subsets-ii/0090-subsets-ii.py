class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        finalSets = []
        nums = sorted(nums)
        def backtrack(i,curSet):
            if i==len(nums):
                finalSets.append(curSet.copy())
                return
            #consider number
            curSet.append(nums[i])
            backtrack(i+1,curSet)
            #dont consider
            curSet.pop(-1)
            while i+1!=len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1,curSet)
        backtrack(0,[])
        return finalSets