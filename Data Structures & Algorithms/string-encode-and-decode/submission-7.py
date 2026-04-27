class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            cnt = len(i)
            res+= f"{cnt}#{i}"
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        while len(s):
            cnt, s = s.split('#',1)
            res.append(s[:int(cnt)])
            s = s[int(cnt):]
        return res

