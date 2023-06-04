class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hm={}
        for char in s:
            if char in hm.keys():
                hm[char]=hm[char]+1
            else:
                hm[char]=1
        for char in t:
            if char in hm.keys():
                hm[char]=hm[char]-1
                if hm[char]==0:
                    del hm[char]
            else:
                return False
        if len(hm)==0:
            return True
        else:
            return False