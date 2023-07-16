class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(low,high,target):
            while low<=high:
                mid = (low+high)//2
                if nums[mid] == target:
                    return mid
                if nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return -1
                    
        left=0
        right= len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>nums[-1]:
                left=mid+1
            else:
                right=mid-1
        pivot=left
        print(pivot)
        left=0
        right = len(nums)-1
        if nums[pivot]<=target<=nums[right]:
            ans = binarySearch(pivot,right,target)
        else:
            ans =  binarySearch(left,pivot,target)
        return ans
            