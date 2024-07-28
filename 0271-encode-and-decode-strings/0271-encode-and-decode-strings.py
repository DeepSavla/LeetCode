class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enStr = ''
        for i in range(len(strs)):
            strs[i] = strs[i].replace('/', '//')
            enStr += strs[i] + '/:'
        return enStr
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        j = 0
        curr = ''
        while j<len(s):
            if s[j] != '/':
                curr += s[j]
                j += 1
            else:
                if s[j + 1] == '/':
                    curr += '/'
                else: 
                    res.append(curr)
                    curr = ''
                j += 2

        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))