class Solution:
    def trap(self, height: List[int]) -> int:
        #finding left-max for each position
        leftMax = [0]
        maxValue =0
        for i in range(1,len(height)):
            if height[i-1] > maxValue:
                maxValue = height[i-1]
            leftMax.append(maxValue)
        #finding right-max for each position
        rightMax = [0]*len(height)
        i=len(height)-2
        maxValue=0
        while i>=0:
            if height[i+1] > maxValue:
                maxValue = height[i+1]
            rightMax[i] = maxValue
            i-=1
        #now calculating water for each position
        totalWater = 0
        for i in range(len(height)):
            curWater =  min(leftMax[i],rightMax[i]) - height[i]
            if curWater>0:
                totalWater = totalWater + curWater
        return totalWater
            
            
        