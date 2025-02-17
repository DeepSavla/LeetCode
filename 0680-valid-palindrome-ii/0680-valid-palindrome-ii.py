class Solution:
    def validPalindrome(self, s: str) -> bool:     
        i = 0 
        j = len(s) - 1
        
        def checkPalindrome(i, j):
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False 
            return True 
        
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return checkPalindrome(i, j-1) or checkPalindrome(i+1, j)
        return True