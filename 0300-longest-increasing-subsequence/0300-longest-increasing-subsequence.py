class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1]*len(nums)
        for i in range(1,len(nums)):
            maxLis = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    maxLis = max(maxLis,LIS[j])
            LIS[i] = 1+maxLis
        return max(LIS)
            
        