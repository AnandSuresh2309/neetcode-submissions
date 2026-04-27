class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS, dictT = {}, {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in dictS.keys():
                    dictS[s[i]] += 1
                else:
                    dictS[s[i]] = 1
                if t[i] in dictT.keys():
                    dictT[t[i]] += 1
                else:
                    dictT[t[i]] = 1
            return dictS == dictT
        else:
            return False