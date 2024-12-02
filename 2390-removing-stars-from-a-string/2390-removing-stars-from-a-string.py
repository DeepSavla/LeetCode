class Solution:
    def removeStars(self, s: str) -> str:
        popCount = 0
        st = []
        for c in s:
            if c =="*":
                if len(s)>0:
                    st.pop()
            else:
                st.append(c)
        print(st)
        return "".join(st)
            
        