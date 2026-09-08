class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        operatorSet = {"+", "*", "/", "-"}

        if len(tokens) == 1 and tokens[0] in operatorSet:
            return 0
        if len(tokens) == 1:
            return int(tokens[0])
        
        # number of operands we have in current operation 

        for i in range(len(tokens)):
            if tokens[i] in operatorSet:
                # this is an operator
                second = stack.pop(-1)
                first = stack.pop(-1)
                computation = 0
                if tokens[i] == "+":
                    computation = first + second
                elif tokens[i] == "*":
                    computation = first * second
                elif tokens[i] == "-":
                    computation = first - second
                elif tokens[i] == "/":
                    computation = int(first / second)         
                stack.append(computation)
            else:
                stack.append(int(tokens[i]))

        return stack[-1]




