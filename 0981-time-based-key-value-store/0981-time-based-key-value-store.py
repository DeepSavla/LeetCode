class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm.keys():
            self.hm[key] = [[timestamp,value]]
        else:
            self.hm[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm.keys():
            return ""
        arr = self.hm[key]
        i=0
        j=len(arr)-1
        mid=0
        res = ""
        while i<=j:
            mid = (i+j)//2
            if arr[mid][0]<=timestamp:
                res = arr[mid][1]
                i=mid+1
            else:
                j=mid-1
        return res
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)