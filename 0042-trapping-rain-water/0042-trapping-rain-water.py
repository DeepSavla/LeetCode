class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0: 
            return 0
        l=0 
        r = len(height) - 1
        leftMax = height[l] 
        rightMax = height[r]
        total = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r]
        
        return total