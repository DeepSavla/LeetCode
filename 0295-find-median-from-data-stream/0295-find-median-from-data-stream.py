class MedianFinder(object):

    def __init__(self):
        self.myStream = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.myStream.append(num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        self.myStream = sorted(self.myStream)
        if len(self.myStream)%2==1:
            return self.myStream[len(self.myStream)//2]
        else:
            mid = len(self.myStream)//2
            return float(self.myStream[mid] + self.myStream[mid-1])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()