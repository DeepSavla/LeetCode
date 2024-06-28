class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hm ={0:0,1:0,2:0}
        for n in nums:
            hm[n] +=1
        for i in range(len(nums)):
            if i<hm[0]:
                nums[i] = 0
            elif i<hm[0]+hm[1]:
                nums[i] = 1
            else:
                nums[i] = 2
            
                