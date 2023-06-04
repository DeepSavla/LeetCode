
class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        diff=0
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in dic.keys()):
                return [dic[diff],i]
            else:
                dic[nums[i]] = i

