class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        k=k+1
        for i in range(k):
            if i < len(nums):
                if nums[i] in s:
                    return True
                else:
                    s.add(nums[i])
        i+=1
        while i<len(nums):
            s.remove(nums[i-k])
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
            i+=1
        return False