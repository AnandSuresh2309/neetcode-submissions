class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += str(l) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res =  []
        num = ""
        i  = 0
        while i < len(s):
            if s[i] !=  '#':
                num += s[i]
            else:
                num  = int(num)
                res.append(s[i+1:i+num+1])
                i+=num
                num = ""
            i+=1
        return res
