class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.size = k
        heapq.heapify(self.minheap)
        for n in nums:
            self.add(n)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.size:
                heapq.heappop(self.minheap)
        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)