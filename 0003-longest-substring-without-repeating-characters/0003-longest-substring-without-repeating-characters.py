class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = len(s)
        longest=0
        hmset= set()
        for i in range(0,l):
            tempLongest = 0
            for j in range(i,l):
                if s[j] in hmset:
                    hmset.clear()
                    break;
                else:
                    hmset.add(s[j])
                    tempLongest = tempLongest +1
                if tempLongest > longest:
                    longest = tempLongest
        return longest
