class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniqueChar = set(s)
        freq = set()
        deletions=0
        print(uniqueChar)
        for setChar in uniqueChar:
            tempCount=0
            for stringChar in s:
                if setChar == stringChar:
                    tempCount = tempCount + 1
            print(tempCount)
            if tempCount in freq:
                while tempCount in freq:
                    tempCount = tempCount-1
                    deletions = deletions+1
                    if tempCount == 0:
                        break
            freq.add(tempCount)
        return deletions
        