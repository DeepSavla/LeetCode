import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        # arr = heapq.nlargest(k, nums)
        # return arr[-1]
        nums = sorted(nums)
        return nums[k*-1]
        