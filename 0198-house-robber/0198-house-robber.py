class Solution:
    def rob(self, nums: List[int]) -> int:
        total = nums.copy()
        for i in range(2,len(nums)):
            prevTotal1=0
            if i-3>=0:
                prevTotal1 = total[i-3]
            prevTotal2 = total[i-2]
            total[i] = max(prevTotal1,prevTotal2)+nums[i]
        return max(total)