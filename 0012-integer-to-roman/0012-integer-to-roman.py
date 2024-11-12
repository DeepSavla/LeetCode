class Solution:
    def intToRoman(self, num: int) -> str:
        mappingArr = [["M",1000],["CM",900],["D",500],["CD",400],["C",100],["XC",90],["L",50],["XL",40],["X",10],["IX",9],["V",5],["IV",4],["I",1]]
        roman = ""
        while num > 0:
            for m in mappingArr:
                if num >= m[1]:
                    roman += m[0]
                    num = num - m[1]
                    break
        return roman