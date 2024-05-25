class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            negative = True
            x=x*-1
        else:
            negative = False
        res = 0
        while x>0:
            dig = x%10
            x = x//10
            res = res*10 +dig
        if negative:
            res=res*-1
        if  -2147483648 <= res <  2147483648:
            return res
        return 0