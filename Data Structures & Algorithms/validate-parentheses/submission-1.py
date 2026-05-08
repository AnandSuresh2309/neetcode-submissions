class Solution:
    def isValid(self, s: str) -> bool:
        l = list()
        bracket = {
            "[":"]",
            "(":")",
            "{":"}"
        }
        for i in s:
            if i in bracket.keys():
                l.append(i)
            else:
                if len(l)>0:
                    j = l.pop()
                    if bracket[j] != i:
                        return False
                else: return False
        if len(l) >0:
            return False
        else:
            return True

