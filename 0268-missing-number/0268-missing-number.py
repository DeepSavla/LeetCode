class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        for number in range(len(nums)+1):
            if number not in num_set:
                return number