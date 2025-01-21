class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        l = 0 #for 0 swap positions
        r = len(nums) -1 #for 2 swap positions
        i = 0 #for iterating
        while i<=r:
            if nums[i] == 0:
                swap(i,l)
                l +=1
                i+=1
            elif nums[i]==2:
                swap(i,r)
                r-=1
            else:
                i+=1
        return nums
