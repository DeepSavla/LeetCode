class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=0
        r=0
        swap = 0
        while r<len(nums):
            if nums[r] ==val:
                r+=1
            else:
                #swap values at l and r
                tempVal = nums[l]
                nums[l] = nums[r]
                nums[r] = tempVal
                #increment l and r
                l+=1
                r+=1
                swap+=1
        return swap

            