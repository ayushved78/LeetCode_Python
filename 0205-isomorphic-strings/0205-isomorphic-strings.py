class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        dic = dict()
        l = len(s)
        for i in range(l):
            if s[i] in dic and dic[s[i]] != t[i]:
                return False
            dic[s[i]] = t[i]
        return True