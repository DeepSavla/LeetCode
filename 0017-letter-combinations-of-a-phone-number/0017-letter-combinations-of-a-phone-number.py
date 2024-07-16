class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {"2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        if digits =="":
            return res
        cur = ""
        def backtrack(i,cur):
            if i==len(digits):
                res.append(cur[:])
                return
            for d in hm[digits[i]]:
                cur = cur + d
                backtrack(i+1,cur)
                cur = cur[:-1]
        backtrack(0,cur)
        return res