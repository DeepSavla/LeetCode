class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        if target>nums[end]:
            return end+1
        while start<=end:
            mid = (start+end)/2
            if nums[mid] == target:
                return mid
            if nums[mid]>target:
                if nums[mid-1]<target:
                    return mid
                else:
                    end = mid-1
            if nums[mid]<target:
                start = mid+1
        return mid
            