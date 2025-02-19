class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm ={}
        for s in strs:
            sortedWord = sorted(s)
            sortedWord = "".join(sortedWord)
            if sortedWord in hm.keys():
                hm[sortedWord].append(s)
            else:
                hm[sortedWord] = [s]
        anagrams = []
        for key in hm.keys():
            anagrams.append(hm[key])
        return anagrams