class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i+1, n+1):
                subarr = arr[i:j]
                if len(subarr) % 2 != 0:
                    res = res + sum(subarr)
        return res