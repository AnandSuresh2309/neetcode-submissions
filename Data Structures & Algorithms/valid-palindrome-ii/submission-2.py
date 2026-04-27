class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        d = 0
        while l<r:
            if s[l] != s[r] and d == 0:
                d += 1
                if s[l+1] == s[r] and s[l] == s[r-1] and len(s)>2:
                    if s[l+2] == s[r-1]:
                        l+=1
                        continue
                    if s[l+1] == s[r-2]:
                        r-=1
                        continue
                elif s[l+1] == s[r]:
                    l += 1
                    continue
                elif s[l] == s[r-1]:
                    r -= 1
                    continue
                else:
                    return False
            elif s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
                
        