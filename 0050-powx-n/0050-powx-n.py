class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n<0:
            return 1/self.myPow(x,-1 *n)
        if n%2==1:
            return x * self.myPow(x,n-1)
        else:
            return self.myPow(x*x,n/2)
'''
Approach:-
Recursive Strategy:
- Divide the problem into smaller parts.
- For even n: the problem size is reduced by half in each step by finding pow(x*x,n/2)
- For odd n : subtract 1 first to make it even.
- for negative n: Convert it to positive i.e. return 1/(pow(x,n))
Note: Squaring x reduces the number of multiplications, making it faster than a naive approach.

Algo:
Recursive solution:
- Base case: if n==0: return 1
- if n is negative: 
    - Convert it to positive
	- return 1/(mypow(x,n))
- if n is positive:
	- if n is odd: 
		- make it even
		-  return n * mypow(x,n-1)
	- if n is even:
		- reduce the claculations to half
		- return mypow(x*x, n/2)

Complexity:
Time and space: O(log(n))
'''