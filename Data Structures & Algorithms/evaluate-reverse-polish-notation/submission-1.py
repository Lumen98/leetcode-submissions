class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # queue = [9, 4]
        opSet = {"+", "*", "-", "/"}
        stack = []

        for tok in tokens:
            if tok not in opSet:
                stack.append(int(tok))
            else:
                b = stack.pop()   # second operand
                a = stack.pop()   # first operand
                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:  # "/"
                    # truncate toward zero
                    stack.append(int(a / b))
        
        return stack[-1]

        
            


        

