class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        res = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j]-nums[i]==diff:
                    for k in range(j,len(nums)):
                        if nums[k]-nums[j]==diff:
                            res=res+1
        return res