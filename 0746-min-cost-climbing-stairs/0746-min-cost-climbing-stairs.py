class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = [0] * (len(cost)+1)
        for i in range(2,len(cost)+1):
            total[i] = min((cost[i-1]+total[i-1]),(cost[i-2]+total[i-2]))
        return total[-1]
        