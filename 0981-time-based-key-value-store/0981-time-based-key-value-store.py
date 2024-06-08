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
        i=len(arr)-1
        res = ""
        while i>=0 and arr[i][0]>timestamp:
            i=i-1
        if arr[i][0]<=timestamp:
            res = arr[i][1]
        return res
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)