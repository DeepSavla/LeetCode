class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(inputString, isOneDeleted):
            l = 0
            r = len(inputString)-1
            while l < r:
                if inputString[l] != inputString[r]:
                    if isOneDeleted == True:
                        return False
                    else:
                        isOneDeleted = True
                        return checkPalindrome(inputString[l+1:r+1], isOneDeleted) or checkPalindrome(inputString[l:r], isOneDeleted)
                else:
                    l+=1
                    r-=1
            return True

        isOneDeleted = False
        return checkPalindrome(s, isOneDeleted)