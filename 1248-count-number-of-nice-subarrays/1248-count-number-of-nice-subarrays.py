class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        totalArr = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        hm={}
        sum=0
        hm[0] = 1
        for j in range(len(nums)):
            sum += nums[j]
            if (sum - k) in hm:
                totalArr += hm[sum - k]
            hm[sum] = hm.get(sum, 0) + 1
        return totalArr
            