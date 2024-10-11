class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largestArr =[]
        heapq.heapify(largestArr)
        for n in nums:
            if len(largestArr)<k:
                heapq.heappush(largestArr,n)
            else:
                if n>largestArr[0]:
                    heapq.heappop(largestArr)
                    heapq.heappush(largestArr,n)
        return largestArr[0]
        