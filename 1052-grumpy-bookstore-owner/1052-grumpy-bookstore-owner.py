#Sliding Window
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfiedCustCount = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                satisfiedCustCount = satisfiedCustCount + customers[i]
        start = minutes
        for i in range(minutes):
            if grumpy[i] == 1:
                satisfiedCustCount = satisfiedCustCount + customers[i]
        maxsatisfiedCustCount = satisfiedCustCount
        while start < len(grumpy):
            if grumpy[start] == 1:
                satisfiedCustCount = satisfiedCustCount + customers[start]
            if grumpy[start-minutes] == 1:
                    satisfiedCustCount = satisfiedCustCount - customers[start-minutes]
            start=start+1
            maxsatisfiedCustCount = max(maxsatisfiedCustCount, satisfiedCustCount)
        return maxsatisfiedCustCount
                    
            