class Solution:
    def rob(self, nums: List[int]) -> int:
        total = nums.copy()
        if len(nums)>2:
            total[2] = nums[2]+total[0]
        for i in range(3,len(nums)):
            total[i] = max(total[i-3],total[i-2])+nums[i]
        print(total)
        return max(total)