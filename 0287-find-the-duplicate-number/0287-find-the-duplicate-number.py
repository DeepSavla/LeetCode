class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sp = nums[0]
        fp = nums[0]
        while 1:
            sp = nums[sp]
            fp = nums[nums[fp]]
            if sp==fp:
                break
        newPtr = nums[0]
        while newPtr!=sp:
            sp = nums[sp]
            newPtr = nums[newPtr]
        return sp