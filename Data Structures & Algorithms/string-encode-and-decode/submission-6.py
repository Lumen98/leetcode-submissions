class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        if len(strs) == 0:
            return sol
        
        for s in strs:
            sol += str(len(s))
            sol += "#"
            sol += s
        return sol

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + length + 1

        return res
            

            








