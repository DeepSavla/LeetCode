class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i=len(a)-1
        j=len(b)-1
        carry = 0
        resArr = []
        while i>=0 or j>=0:
            if i<0:
                dig1 = 0
            else:
                dig1 = a[i]
            if j<0: 
                dig2 = 0
            else:
                dig2 = b[j]
            res = int(dig1) + int(dig2) + carry
            if res<=1:
                carry=0
            if res ==2:
                res=0
                carry = 1
            if res ==3:
                res=1
                carry =1
            resArr.append(str(res))
            i=i-1
            j=j-1
        if carry ==1:
            resArr.append("1")
        resArr = resArr[::-1]
        res = ""
        return res.join(resArr)
                