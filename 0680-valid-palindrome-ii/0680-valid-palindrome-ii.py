class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(l,r, isOneDeleted):
            while l < r:
                if s[l] != s[r]:
                    if isOneDeleted == True:
                        return False
                    else:
                        isOneDeleted = True
                        return checkPalindrome(l+1,r, isOneDeleted) or checkPalindrome(l,r-1, isOneDeleted)
                else:
                    l+=1
                    r-=1
            return True

        isOneDeleted = False
        l = 0
        r = len(s)-1
        return checkPalindrome(l, r, isOneDeleted)