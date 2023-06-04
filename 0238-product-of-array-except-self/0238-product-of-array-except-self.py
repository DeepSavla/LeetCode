class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix=[]
        postfix=[]
        product=1
        resArr=[]
        lenIp = len(nums)
        for i in range(lenIp):
            product = product*nums[i]
            prefix.append(product)
        product=1
        for i in range(lenIp-1,-1,-1):
            product = product*nums[i]
            postfix.insert(0,product)
        for i in range(lenIp):
            if i==0:
                res = postfix[1]
            elif i== (lenIp-1):
                res = prefix[lenIp-2]
            else:
                res= prefix[i-1]*postfix[i+1]
            resArr.append(res)
        return resArr
                