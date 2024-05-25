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
        x=str(x)
        x= x[::-1]
        x= int(x)
        if negative:
            x=x*-1
        if  -2147483648 <= x <  2147483648:
            return x
        return 0