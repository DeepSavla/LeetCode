class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        res1=""
        res2=""
        for i in word1:
            res1 = res1 + i
        for i in word2:
            res2 = res2 + i
        if res1==res2:
            return True
        else:
            return False