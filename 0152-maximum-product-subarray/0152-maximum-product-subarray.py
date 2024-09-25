class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxTillNow = nums[0]
        minTillNow = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==0:
                maxTillNow = 1
                minTillNow = 1
            temp = maxTillNow *nums[i]
            maxTillNow = max(temp, minTillNow*nums[i], nums[i])
            minTillNow = min(temp, minTillNow*nums[i], nums[i])
            result = max(result,maxTillNow)
        return result