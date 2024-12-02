class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums)-1
        evenRightLength = False
        while low < high:
            mid = (high+low)//2
            if (high-mid)%2==0:
                evenRightLength = True
            else:
                evenRightLength = False
            if nums[mid+1]==nums[mid]:
                if evenRightLength:
                    #skip all occurences of current number
                    low=mid+2 
                else:
                    high=mid-1
            elif nums[mid-1]==nums[mid]:
                if evenRightLength:
                    high=mid-2
                else:
                    low=mid+1
            else:
                return nums[mid]
        return nums[low]
            