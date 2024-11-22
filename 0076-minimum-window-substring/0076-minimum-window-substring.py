class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmTarget = {}
        hmHave = {}
        minLength = math.inf
        res = ""
        for letter in t:
            if letter not in hmTarget:
                hmTarget[letter] = 0
            hmTarget[letter]+=1
        lettersToMatch = len(hmTarget)
        currentLettersMatched = 0
        j=0
        i=0
        while j<len(s):
            if s[j] in hmTarget:
                if s[j] not in hmHave:
                    hmHave[s[j]] = 0
                hmHave[s[j]]+=1
                if hmHave[s[j]] ==hmTarget[s[j]]:
                    #equal comparison bec. equal will always be only once
                    currentLettersMatched +=1
            while currentLettersMatched==lettersToMatch:
                if j-i+1 < minLength:
                    minLength = j-i+1
                    res = s[i:j+1]
                #increment i till the substring is not matched in window
                if s[i] in hmHave:
                    hmHave[s[i]] -=1
                    if hmHave[s[i]] < hmTarget[s[i]]:
                        currentLettersMatched -=1
                i+=1
            j+=1
            
        return res
                
            
        