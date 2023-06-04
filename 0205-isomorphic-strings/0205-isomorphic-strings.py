class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hm ={}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hm.keys():
                hm[s[i]] = t[i]
            else:
                if hm[s[i]] != t[i]:
                    return False
        keys = hm.keys()
        for key in range(len(keys)):
            for nextKey in range(key+1,len(keys)):
                if hm[keys[key]] == hm[keys[nextKey]]:
                    return False
        return True
