class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = "" 

        for word in strs:
            res += str(len(word))
            res += "#"
            res += word
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        length = 0
        
        while index < len(s): 
            length = ""
            while s[index] != "#":
                length += s[index]
                index += 1

            length = int(length)

            word = s[index + 1 : index + length + 1]

            res.append(word)

            index += length + 1
        
        return res
                




