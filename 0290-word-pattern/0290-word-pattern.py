class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        hm={}
        i=0
        words = set()
        if len(pattern) != len(s):
            return False
        while i<len(s):
            if pattern[i] not in hm.keys():
                hm[pattern[i]] = s[i]
                if s[i] in words:
                    return False
                else:
                    words.add(s[i])
            else:
                if hm[pattern[i]]!=s[i]:
                    return False
            i+=1
        return True
        