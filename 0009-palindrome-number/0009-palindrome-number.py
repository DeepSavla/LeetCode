class Solution(object):
    def isPalindrome(self, x):
        arr = []
        x = str(x)
        for dig in x:
            arr.append(dig)
        length = len(arr)
        palindrome= True
        for i in range(length/2):
            if(arr[i] != arr[length-i-1]):
                palindrome= False
        return palindrome
        