class Solution(object):
    def mySqrt(self, x):
        l=0
        r=x
        while l<=r:
            mid=(l+r)//2
            sq=mid*mid
            sq1=(mid+1)*(mid+1)         
            if sq<=x and  sq1>x:
                return mid
            elif sq>x:
                r=mid-1
            else:
                l=mid+1

        