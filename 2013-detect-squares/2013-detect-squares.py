class DetectSquares:

    def __init__(self):
        self.allPoints ={}

    def add(self, point: List[int]) -> None:
        pointTuple = (point[0],point[1])
        if (pointTuple) in self.allPoints:
            self.allPoints[pointTuple] +=1
        else:
            self.allPoints[pointTuple] =1
        
    #for every point given consider each stored point and diagonal and find if other two points exist or not. if they exist multiply count of every point to find number of squares. add the results as there can be multiple squares.
    def count(self, point: List[int]) -> int:
        px = point[0]
        py = point[1]
        res = 0
        for p in self.allPoints.keys():
            if abs(p[0]-px) == abs(p[1]-py) and p[0]!=px and p[1]!=py:
                if (p[0],py) in self.allPoints and (px,p[1]) in self.allPoints:
                    res += self.allPoints[(p[0],py)] * self.allPoints[(px,p[1])] * self.allPoints[(p[0],p[1])]
        return res
            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)