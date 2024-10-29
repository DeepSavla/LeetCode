class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        sum=0
        totalArrays =0
        for n in nums:
            sum = sum+n
            if sum-k in prefixSum:
                totalArrays = totalArrays + prefixSum[sum-k]
            if sum in prefixSum.keys():
                prefixSum[sum] = prefixSum[sum]+1
            else:
                prefixSum[sum] = 1
        return totalArrays
        