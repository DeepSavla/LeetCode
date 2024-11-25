class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1: #handling for case where k=1
            return True
        s = set() #to note indexes of increasing sunArr of length k
        curIncreasingCount = 1 #initial length is 1
        for i in range (1,len(nums)):
            if nums[i]>nums[i-1]:
                curIncreasingCount +=1
                if curIncreasingCount>=k:
                    if i-k-k+1 in s:
                        return True
                    else:
                        s.add(i-k+1)
            else:
                curIncreasingCount = 1
        
            
                    
        