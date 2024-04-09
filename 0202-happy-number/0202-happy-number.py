class Solution:
    def isHappy(self, n: int) -> bool:
        resSet = set()
        res=0
        while res !=1:
            res = self.findSquareSum(n)
            CurLen = len(resSet)
            resSet.add(res)
            n=res
            if CurLen == len(resSet):
                return False
        return True
            
            
    def findSquareSum(self,number):
        sum=0
        while number>=1:
            dig = number%10
            sum = sum + (dig*dig)
            number = number//10
        return sum