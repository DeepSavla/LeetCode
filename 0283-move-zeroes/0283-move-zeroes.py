class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=1
        i=0
        while j < len(nums):
            if nums[j]==0 or i==j:
                j=j+1
            else:
                if nums[i] == 0:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                    j=j+1
                i=i+1
            