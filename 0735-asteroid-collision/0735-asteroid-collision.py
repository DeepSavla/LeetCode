class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        
        for a in asteroids:
            # Process collisions
            while s and s[-1] > 0 and a < 0:
                if abs(s[-1]) < abs(a):
                    s.pop()  # Pop smaller asteroid from stack
                    continue
                elif abs(s[-1]) == abs(a):
                    s.pop()  # Both asteroids explode
                break
            else:
                # If no collision, add the asteroid to the stack
                s.append(a)
        return s