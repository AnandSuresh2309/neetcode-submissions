class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in strs:
                if len(j) > i:
                    if j[i] != char:
                        return res
                else:
                    return res
            res += char
        return res