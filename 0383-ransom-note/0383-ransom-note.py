class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = {}
        
        for char in magazine:
            if char in hm.keys():
                hm[char] = hm[char] +1
            else:
                hm[char] = 1
                
        for char in ransomNote:
            if char in hm.keys():
                if hm[char] ==1:
                    del hm[char]
                else:
                    hm[char] = hm[char]-1
            else:
                return False
        return True