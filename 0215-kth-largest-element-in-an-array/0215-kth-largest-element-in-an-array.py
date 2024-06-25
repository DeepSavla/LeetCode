import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr =[]
        heapq.heapify(arr)
        for n in nums:
            if len(arr)<k:
                heapq.heappush(arr,n)
            else:
                if arr[0] < n:
                    heapq.heappop(arr)
                    heapq.heappush(arr,n)
        return heapq.heappop(arr)
            
                
        