class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-k-k+1):
            found = None
            for j in range(i+1, i+k):
                if nums[j]<=nums[j-1]:
                    found = False
            for j in range(i+k+1,i+k+k):
                if nums[j]<=nums[j-1]:
                    found = False
            if found != False:
                return True
                    
        