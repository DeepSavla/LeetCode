class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 1
        resStr = s[0]
        n = len(s)
        for i in range(n):
            #checking odd length palindrome
            left = i-1
            right = i+1
            while left>=0 and right<n and s[left]==s[right]:
                if right-left+1>maxLen:
                    maxLen = right-left+1
                    resStr= s[left:right+1]
                left-=1
                right+=1
            #checking even length palindrome
            left=i-1
            right=i
            while left>=0 and right<n and s[left]==s[right]:
                if right-left+1>maxLen:
                    maxLen = right-left+1
                    resStr= s[left:right+1]
                left-=1
                right+=1
        return resStr
            
        
            
            