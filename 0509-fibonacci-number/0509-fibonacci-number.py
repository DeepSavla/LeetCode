class Solution(object):
    def fib(self, n):
        result = 0
        if n==0:
            result =0
        elif n==1:
            result=1
        else:
            result = self.fib(n-1) + self.fib(n-2)
        return result