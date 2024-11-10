import random
class RandomizedSet:

    def __init__(self):
        self.hm={}
        self.arr=[]
        

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        self.hm[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val  not in self.hm.keys():
            return False
        idx = self.hm[val]
        lastEle = self.arr[-1]
        self.arr[idx] = lastEle
        self.hm[lastEle] = idx
        del self.hm[val]
        self.arr.pop()
        return True
            

    def getRandom(self) -> int:
        r = random.randint(1, 10) #to get a random number
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()