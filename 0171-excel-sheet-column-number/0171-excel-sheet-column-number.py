class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        sum=0
        i=0
        for letter in columnTitle[::-1]:
            sum = sum + 26**i * (ord(letter) - 64) 
            i=i+1
        return sum