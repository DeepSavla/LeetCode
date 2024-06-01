class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(None)
        i=0
        j=len(nums)-1
        idx = j
        while i<=j:
            if abs(nums[i])>abs(nums[j]):
                ans[idx] = nums[i]*nums[i]
                i+=1
            else:
                ans[idx] = nums[j]*nums[j]
                j-=1
            idx -=1
        return ans
        