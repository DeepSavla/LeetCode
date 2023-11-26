class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        resString = s[0]
        
        def expand(i,j):
            while i>=0 and j<len(s) and s[i] == s[j]:
                i = i-1
                j=j+1
            return s[i+1:j]
            
        for i in range(len(s)):
            evenString = expand(i,i+1)
            if len(evenString)>len(resString):
                resString = evenString
            oddString = expand(i-1,i+1)
            if len(oddString)>len(resString):
                resString = oddString
        return resString
            
            