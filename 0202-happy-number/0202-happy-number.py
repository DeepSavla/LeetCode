class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSqOfDigits(n):
            sum = 0
            while n>0:
                d = n%10
                sum = sum + (d*d)
                n=n//10
            return sum
        
        s = set()
        s.add(n)
        while 1:
            n = sumOfSqOfDigits(n)
            if n==1:
                return True
            if n in s:
                return False
            else:
                s.add(n)
                
            
        
                
        
        
        
        
'''
- initialize a set
- add n to set
- while true:
    - n = calculate the sum of squares of n
    - if n in set: 
        - return false  #coz this will happen infinitely
    - if it is 1 return true
'''