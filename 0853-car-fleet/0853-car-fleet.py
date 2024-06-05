class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeedArr = []
        lenCars = len(position)
        for i in range(lenCars):
            posSpeedArr.append([position[i],speed[i]])
        posSpeedArr = sorted(posSpeedArr)
        posSpeedArr = posSpeedArr[::-1]
        fleet = []
        for c in posSpeedArr:
            t = (target- c[0])/c[1]
            if len(fleet)==0 or t>fleet[-1]:
                fleet.append(t)
        return len(fleet)
                
            