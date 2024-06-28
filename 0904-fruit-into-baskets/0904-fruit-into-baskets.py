class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruits = 0
        i=0
        j=0
        basket = {}
        while j<len(fruits):
            if len(basket)<=2:
                if fruits[j] in basket:
                    basket[fruits[j]] += 1
                else:
                    basket[fruits[j]] = 1
                j+=1
            else:
                while len(basket)>2:
                    if basket[fruits[i]] == 1:
                        del basket[fruits[i]]
                    else:
                        basket[fruits[i]] -= 1
                    i+=1
            if len(basket) <=2:
                maxFruits = max(maxFruits, j-i)
        return maxFruits
                    
            
            
        