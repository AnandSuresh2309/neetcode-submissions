class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(a,b):
            if len(a) == len(b):
                print(a, b)
                for e in b.keys():
                    if a[e] < b[e]:
                        return False
                return True
            return False
        ct = 1001
        res = ""
        tset = {}
        wset = {}
        l = 0
        for a in t:
            tset[a] = 1 + tset.get(a,0)
        for r in range(len(s)):
            if s[r] in tset:
                wset[s[r]] = 1 + wset.get(s[r],0)

            while check(wset,tset) and len(s[l:r+1])>=len(t):
                
                res = s[l:r+1] if ct > len(s[l:r+1]) else res
                ct = len(res)
                l += 1
                
                wset = {}
                for x in range(l,r+1):
                    if s[x] in tset:
                        wset[s[x]] = 1 + wset.get(s[x],0)
            
            print(r, res)
        return res if len(res)>=len(t) else ""
            
            
            





        