class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict, r_dict  = {}, {}
        for i,j in zip(s,t):
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
            if j in r_dict:
                r_dict[j] += 1
            else:
                r_dict[j] = 1
        for key in s_dict.keys():
            if key in r_dict.keys():
                if s_dict[key] != r_dict[key]:
                    return False
            else:
                return False
        return True
