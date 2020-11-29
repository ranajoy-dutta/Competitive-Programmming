class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """ 
        prefix=""
        if len(strs)==0: return prefix

        for i in range(len(min(strs))):
            c=strs[0][i]
            if all(a[i]==c for a in strs):
                prefix+=c
            else:
                break
        return prefix
