class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { "]":"[", "}":"{", ")":"(" }
        stack = []

        for c in s:
            if c in hashmap.values():
                stack.append(c)
            else:
                if c in hashmap.keys():
                    if not stack:
                        return False
                    if stack.pop(-1) != hashmap[c]:
                        return False
                else:
                    return False
        
        if stack:
            return False
        return True

             
        