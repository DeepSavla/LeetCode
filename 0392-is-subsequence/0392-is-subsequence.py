class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lenSub = len(s)
        lenStr = len(t)
        i = 0
        j=0
        while i<lenSub and j<lenStr:
            if s[i] == t[j]:
                i = i+1
                j = j+1
            else:
                j=j+1
        if i == len(s):
            return True
        else:
            return False
                