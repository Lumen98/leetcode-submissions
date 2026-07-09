class Solution:
    '''
        #<length><word> #<length><word>
    '''
    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s += str(len(word)) + "#"  + word

        return s

    def decode(self, s: str) -> List[str]:

        res = []

        r = 0

        while r < len(s):
            l = r

            while r < len(s) and s[r] != "#":
                r += 1
            

            if r > len(s):
                break
            
            length = int(s[l:r])

            word = s[r + 1:r + 1 + length]

            res.append(word)
            
            r = r + 1 + length
            
        
        return res







