class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r,i = 0,0,0
        res = ""
        while i < len(word1)+len(word2):
            if l < len(word1) and r < len(word2):
                res += word1[l]+word2[r]
                l+=1
                r+=1
            elif l < len(word1):
                res += word1[l]
                l+=1
            elif r < len(word2):
                res += word2[r]
                r+=1
            i+=1
        return res