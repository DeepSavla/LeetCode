class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        def backtrack(i,cur):
            if i == len(s):
                res.append(cur.copy())
                return
            for j in range(i,len(s)):
                tempStr = s[i:j+1]
                if tempStr == tempStr[::-1]:
                    cur.append(tempStr)
                    backtrack(j+1,cur)
                    cur.pop()
        backtrack(0,cur)
        return res