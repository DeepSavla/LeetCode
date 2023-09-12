class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start=0
        end=len(numbers)-1
        while start<end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start+1,end+1]
            elif sum>target:
                end=end-1
            else:
                start = start+1
        