class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        lenN = len(nums)
        res=set()
        for i in range(lenN-2):
            j=i+1
            k=lenN-1
            while j<k:
                sum = nums[i] + nums[j] + nums[k]
                if sum==0:
                    res.add((nums[i],nums[j],nums[k]))
                    j=j+1
                    k=k-1
                elif sum>0:
                    k=k-1
                else:
                    j=j+1
        return list(res)