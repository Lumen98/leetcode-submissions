class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        hashmap = {")":"(", "}":"{", "]":"["}


        stack = []


        for c in s:
            if c in hashmap:
                # closing brac
                if stack and stack[-1] == hashmap[c]:
                    stack.pop(-1)
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        if not stack:
            return True
        
        return False

          



