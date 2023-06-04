class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1
        while(i>=0):
            if digits[i]<9:
                digits[i]+=1
                break
            else:
                if i==0 and digits[0] ==9:
                    digits[0] =0
                    digits.insert(0,1)
                    break
                else:
                    digits[i] =0
            i=i-1
        return digits