class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        
        for a in asteroids:
            # Process collisions
            #checking only positive in stack bec 
            #negative before positive will go in left without coliding
            while 1:
                if len(s)>0 and s[-1] > 0 and a < 0:
                    if  abs(a)>abs(s[-1]):
                        s.pop()  # Pop smaller asteroid from stack
                        continue
                    elif abs(s[-1]) == abs(a):
                        s.pop()  # Both asteroids explode
                    break
                else:
                    # If no collision, add the asteroid to the stack
                    s.append(a)
                    break
        return s