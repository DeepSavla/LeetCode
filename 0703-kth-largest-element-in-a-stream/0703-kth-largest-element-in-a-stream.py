class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.size = k
        heapq.heapify(self.minheap)
        for n in nums:
            self.add(n)
        
        

    def add(self, val: int) -> int:
        if len(self.minheap) < self.size:
            heapq.heappush(self.minheap, val)
        else:
            if val > self.minheap[0]:
                heapq.heappop(self.minheap)
                heapq.heappush(self.minheap, val)
        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)