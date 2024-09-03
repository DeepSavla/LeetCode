class Solution:
    def countSubstrings(self, s: str) -> int:
        maxLen = 1
        resStr = []
        n = len(s)
        for i in range(n):
            #checking odd length palindrome
            resStr.append(s[i])
            left = i-1
            right = i+1
            while left>=0 and right<n and s[left]==s[right]:
                resStr.append(s[left:right+1])
                left-=1
                right+=1
            #checking even length palindrome
            left=i-1
            right=i
            while left>=0 and right<n and s[left]==s[right]:
                resStr.append(s[left:right+1])
                left-=1
                right+=1
        return len(resStr)