import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        MinLen = math.inf
        sum=0
        while j<len(nums):
            if i==j:
                if nums[i]>=target:
                    return 1
                else:
                    j=j+1
                    if j<len(nums):
                        sum = nums[i]+nums[j]
            else:
                if  sum >= target:
                    curMinLength = j-i+1
                    MinLen = min(MinLen , curMinLength)
                    sum = sum - nums[i]
                    i=i+1
                else:
                    j=j+1
                    if j<len(nums):
                        sum = sum + nums[j]
        if MinLen == math.inf:
            return 0
        return MinLen
            
                    