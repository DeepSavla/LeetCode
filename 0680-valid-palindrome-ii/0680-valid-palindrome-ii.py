class Solution(object):
    def validPalindrome(self, s):
        i=0
        j=len(s)-1
        while(i<j):
            if s[i]==s[j]:
                i=i+1
                j=j-1
            else:
                break
        if(i>=j):
            return True
        else:
            newStr = s[i:j]
            if newStr == newStr[::-1]:
                return True
            newStr = s[i+1:j+1]
            if newStr == newStr[::-1]:
                return True
