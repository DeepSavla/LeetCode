class Solution:
    def rob(self, nums: List[int]) -> int:
        total = nums.copy()
        for i in range(2,len(nums)):
            prevMax=0
            for j in range(i-1):
                prevMax = max(prevMax,total[j])
            total[i] = prevMax + nums[i]
        return max(total)