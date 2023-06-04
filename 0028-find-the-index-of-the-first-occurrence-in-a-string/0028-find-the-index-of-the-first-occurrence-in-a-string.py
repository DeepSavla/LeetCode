class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenNeedle = len(needle)
        lenHaystack = len(haystack)
        i=0
        while i<=lenHaystack-lenNeedle:
            if haystack[i:lenNeedle+i] == needle:
                return i
                break
            else:
                i+=1
        return -1

        