class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False] * (len(s)+1)
        memo[len(s)] = True
        i=len(s)-1
        while i>=0:
            for w in wordDict:
                if len(w)<=len(s)-i:
                    if w==s[i:i+len(w)]:
                        memo[i] = memo[i+len(w)]
                if memo[i]==True:
                    break
            i-=1
        print(memo)
        return memo[0]