class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        stack.append([s[0],1])
        for i in range(1,len(s)):
            if len(stack)>0 and s[i] == stack[-1][0]:
                stack[-1][1] = stack[-1][1] + 1
            else:
                stack.append([s[i],1])
            if stack[-1][1] == k:
                stack.pop()
        str=""
        for i in range(len(stack)):
            for j in range(stack[i][1]):
                str = str + stack[i][0]
        return str
        
                    