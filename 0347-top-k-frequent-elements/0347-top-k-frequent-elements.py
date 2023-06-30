class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hm={}
        op =[]
        for val in nums:
            if val in hm.keys():
                hm[val] = hm[val]+1
            else:
                hm[val]= 1
        print(hm)
        for count in range(k):
            max=-1
            for values in hm.keys():
                if hm[values]>max:
                    max=hm[values]
                    ele = values
            del hm[ele]
            op.append(ele)
        return op    
        