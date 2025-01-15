class Solution:
    def __init__(self, w: List[int]):
        self.probability = []
        self.weights = w
        self.sum = 0
        for i in self.weights:
            self.sum = self.sum+i
            self.probability.append(self.sum)
        

    def pickIndex(self) -> int:
        #random number gives between 0 and 1
        randomNumber = random.random() * self.sum 
        for i in range(len(self.weights)):
            if randomNumber <= self.probability[i]:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()