class Solution:
    def isUgly(self, n: int) -> bool:
        prevN = 0
        while n!=prevN:
            prevN = n
            if n % 2==0:
                n=n/2
            if n%3 == 0:
                n=n/3
            if n%5 == 0:
                n=n/5
            if n==1:
                return True
        return False
        