class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hmPattern={}
        hmWords={}
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if pattern[i] in hmPattern.keys() and words[i] in hmWords.keys():
                if hmPattern[pattern[i]] != words[i]:
                    return False
                if hmWords[words[i]] != pattern[i]:
                    return False
            else:
                hmPattern[pattern[i]] = words[i]
                hmWords[words[i]] = pattern[i]
        if len(hmPattern.keys()) != len(hmWords.keys()):
            return False
        return True