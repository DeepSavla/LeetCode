# For each string, count how many times each character appears.
# Convert this count array (of fixed length 26) into a tuple to use as a unique signature (hashable key).
# Store the original string in a dictionary keyed by this signature.
# Finally, return all the grouped strings.
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for i in strs:
            ans = [0]*26
            res = []
            for c in i:
                ans[ord(c) - ord("a")] += 1
            if tuple(ans) not in hm:
                hm[tuple(ans)] = [] 
            hm[tuple(ans)].append(i) 
        res = []
        for k in hm.keys():
            res.append(hm[k])
        return res